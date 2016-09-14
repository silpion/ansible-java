#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) Mark Kusch <mark.kusch@silpion.de>


DOCUMENTATION = '''
---
module: keystore
short_description: Manage certificates with Java jks keystore
extends_documentation_fragment: files
description:
  - The M(keystore) module allows to install and uninstall certificates in a Java keystore with keytool
options:
  state:
    description:
      - Whether a certificate should be C(present) or C(absent)
    required: false
    default: present
    choices: [present, absent]
  path:
    description:
      - Path to the keystore file beeing managed. Aliases: I(dest)
    required: true
    default: None
    aliases: ['dest', 'name']
  create:
    description:
      - Whether to create a new keystore if it does not exist.
    required: false
    default: true
  alias:
    description:
      - Alias name or ID for the certificate inside the keystore.
    required: true
    default: None
  crt:
    description:
      - Path to a file containing the SSL certificate, mandatory when state=present
    required: false
    default: None
  password:
    description:
      - Password for the keystore
    required: true
    default: None
  keytool:
    description:
      - Path to a Java keytool for performing operations (required when keytool not in PATH)
    required: false
    default: None
  copy:
    description:
      - Whether to copy files to the remote host
    required: false
    default: True
  creates:
    description:
      - A filename, when it already exists, this step will B(not) be run.
# informational: requirements for nodes
requirements: []
author: Mark Kusch
todo:
  - implementation for truststore vs keystore
  - whether to install pkcs12 and convert to jks with openssl
notes:
  - requires keytool either in $PATH or supplied with keytool= argument
  - does not allow to install private keys
'''


EXAMPLES = '''
- keystore: state=present path=/etc/app/cacerts owner=foo group=foo mode=0644 alias=foo crt=/tmp/app.crt
- keystore: state=absent dest=/etc/app/cacerts alias=bar
'''


import os


class Keystore(object):

    def __init__(self, module, keytool):
        self.module = module
        self.state = module.params['state']
        self.path = os.path.expanduser(module.params['path'])
        self.create = module.boolean(module.params['create'])
        self.alias = module.params['alias']
        self.crt = os.path.expanduser(module.params['crt'])
        self.keytool = keytool
        self.password = module.params['password']
        self.copy = module.boolean(module.params['copy'])
        self.creates = module.params['creates']
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
            state = dict(required=False, choices=['present', 'absent'], type='str', default='present'),
            path = dict(required=True, aliases=['name', 'dest'], type='str'),
            create = dict(required=False, type='bool', default=True),
            alias = dict(required=True, type='str'),
            crt = dict(required=False, type='str', default=None),
            keytool = dict(required=False, type='str', default=None),
            password = dict(required=True, type='str', default=None),
            copy = dict(required=False, type='bool', default=True),
            creates = dict(required=False, type='str', default=None),
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )


    keytool = None
    keytool = module.get_bin_path('keytool', False)
    if keytool is None and module.params['keytool'] is not None:
        if os.path.isfile(module.params['keytool']) and os.access(module.params['keytool'], os.X_OK):
            keytool = module.params['keytool']
    if keytool is None:
        module.fail_json(msg='cannot execute keytool: no such file or directory')


    keystore = Keystore(module, keytool)
    rc = None
    out = ''
    err = ''
    result = {}
    result['path'] = keystore.path
    result['state'] = keystore.state


    if not os.path.exists(keystore.crt):
        if keystore.copy:
            module.fail_json(msg="File '%s' failed to transfer" % os.path.basename(keystore.crt))
    if not os.access(keystore.crt, os.R_OK):
        module.fail_json(msg="File '%s' is not readable" % os.path.basename(keystore.crt))


    if keystore.state == 'absent':
        if keystore.is_crt():
            if module.check_mode:
                module.exit_json(changed=True)
            (rc, out, err) = keystore.crt_del()
            if rc != 0:
                module.fail_json(name=keystore.alias, msg=err)


    elif keystore.state == 'present':
        if not keystore.is_crt():
            if not keystore.exists() and not keystore.create:
                module.exit_json(changed=False, msg='Not creating new keystore (use create=yes)')
            if module.check_mode:
                module.exit_json(changed=True)
            (rc, out, err) = keystore.crt_add()
            if rc != 0:
                module.fail_json(name=keystore.alias, msg=err)


    keystore.set_fs_attributes_if_different(rc)

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
