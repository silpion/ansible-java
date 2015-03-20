#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO implement certificate private keys
# TODO implement copy={true,false}
# TODO truststore vs keystore

import sys
import os

try:
    import selinux
    HAVE_SELINUX=True
except ImportError:
    HAVE_SELINUX=False

DOCUMENTATION = '''
---
module: keystore
short_description: Manage certificates with Java jks keystore
options:
  state:
    description:
      - Whether a certificate should be C(present) or C(absent)
    required: false
    default: present
    choices: [present, absent]
  path:
    description:
      - 'Path to the keystore file beeing managed. Aliases: I(dest)'
    required: true
    default: None
    aliases: ['dest']
  copy:
    description:
      - 'Whether to copy certificates to the managed node. (NOT IMPLEMENTED YET)'
    required: false
    default: true
  create:
    description:
      - 'Whether to create a new keystore if it does not exist.'
    required: false
    default: true
  alias:
    description:
      - 'Alias name or ID for the certificate inside the keystore.'
    required: true
    default: None
    aliases: ['name']
  crt:
    description:
      - 'Path to a file containing the SSL certificate, mandatory when state=present'
    required: false
    default: None
  key:
    description:
      - 'Path to a file containing a SSL certificate key'
    required: false
    default: None
  password:
    description:
      - 'Password for the keystore'
    required: true
    default: None
  keytool:
    description:
      - 'Path to a Java keytool for performing operations'
    required: true
    default: None
# informational: requirements for nodes
requirements: []
author: Mark Kusch
'''

EXAMPLES = '''
- keystore: state=present path=/etc/app/cacerts owner=foo group=foo mode=0644 alias=foo crt=/tmp/app.crt
- keystore: state=absent dest=/etc/app/cacerts alias=bar
'''

class Keystore(object):

    def __init__(self, module):
        self.module = module
        self.state = module.params['state']
        self.path = os.path.expanduser(module.params['path'])
        self.copy = module.boolean(module.params['copy'])
        self.create = module.boolean(module.params['create'])
        self.alias = module.params['alias']
        self.crt = module.params['crt']
        self.key = module.params['key']
        self.keytool = module.params['keytool']
        self.password = module.params['password']
        self.file_args = module.load_file_common_arguments(module.params)

    def exists(self):
        return os.path.isfile(self.path)

    def is_crt(self):
        if self.exists():
            cmd = [self.keytool]
            cmd.append('-noprompt')
            cmd.append('-list')
            cmd.append('-keystore')
            cmd.append(self.path)
            cmd.append('-storepass')
            cmd.append(self.password)
            cmd.append('-alias')
            cmd.append(self.alias)
            (rc, out, err) = self.module.run_command(cmd)
            if rc == 0:
                return True
        return False


    def crt_add(self):
        if not self.is_crt():
            if not self.crt:
                self.module.fail_json(name=self.alias, msg='crt is required when adding certificates')
            else:
                cmd = [self.keytool]
                cmd.append('-noprompt')
                cmd.append('-keystore')
                cmd.append(self.path)
                cmd.append('-trustcacerts')
                cmd.append('-import')
                cmd.append('-file')
                cmd.append(self.crt)
                cmd.append('-alias')
                cmd.append(self.alias)
                cmd.append('-storepass')
                cmd.append(self.password)
                return self.module.run_command(cmd)

    def crt_del(self):
        if self.is_crt():
            cmd = [self.keytool]
            cmd.append('-noprompt')
            cmd.append('-keystore')
            cmd.append(self.path)
            cmd.append('-storepass')
            cmd.append(self.password)
            cmd.append('-alias')
            cmd.append(self.alias)
            cmd.append('-delete')
            return self.module.run_command(cmd)

    def set_fs_attributes_if_different(self, changed):
        return self.module.set_fs_attributes_if_different(self.file_args, changed)


def main():
    module = AnsibleModule(
        argument_spec = dict(
            state = dict(default='present', choices=['present', 'absent'], type='str'),
            path = dict(aliases=['dest'], required=True, type='str'),
            copy = dict(default=True, choices=BOOLEANS),
            create = dict(default=True, choices=BOOLEANS),
            alias = dict(aliases=['name'], required=True, type='str'),
            crt = dict(required=False, default=None, type='str'),
            key = dict(required=False, default=None, type='str'),
            keytool = dict(required=True, default=None, type='str'),
            password = dict(required=True, default=None, type='str'),
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )

    keystore = Keystore(module)
    rc = None
    out = ''
    err = ''
    result = {}
    result['path'] = keystore.path
    result['state'] = keystore.state


    if not os.path.isfile(keystore.keytool) or not os.access(keystore.keytool, os.X_OK):
        module.fail_json(msg='cannot execute keytool at %s' % str(keystore.keytool))


    if keystore.state == 'absent':
        if keystore.is_crt():
            if module.check_mode:
                module.exit_json(changed=True)
            (rc, out, err) = keystore.crt_del()
            if rc != 0:
                module.fail_json(name=keystore.alias, msg=err)


    elif keystore.state == 'present':
        if not keystore.is_crt():
            if module.check_mode:
                if not keystore.exists() and not keystore.create:
                    module.exit_json(changed=False, msg='Not creating new keystore (use create=yes)')
                else:
                    module.exit_json(changed=True)

            if not keystore.exists() and not keystore.create:
                module.exit_json(changed=False, msg='Not creating new keystore (use create=yes)')

            (rc, out, err) = keystore.crt_add()
            if rc != 0:
                module.fail_json(name=keystore.alias, msg=err)


    rc = keystore.set_fs_attributes_if_different(rc)

    if rc is None:
        result['changed'] = False
    else:
        result['changed'] = True
    if out:
        result['out'] = out
    if err:
        result['err'] = err

    module.exit_json(**result)


from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
