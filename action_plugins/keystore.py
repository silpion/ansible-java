# (c) 2015, Mark Kusch <mark.kusch@silpion.de>

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import os
from ansible.plugins.action import ActionBase
from ansible.utils.boolean import boolean


class ActionModule(ActionBase):

    TRANSFER_FILES = True

    def run(self, tmp=None, task_vars=None):
        ''' handler for file transfer operations '''

        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)

        crt = self._task.args.get('crt', None)
        copy = self._task.args.get('copy', True)
        creates = self._task.args.get('creates', None)

        # this module requires at least the crt= to be present
        if crt is None:
            result['failed'] = True
            result['msg'] = "crt is required"
            return result

        remote_user = task_vars.get('ansible_ssh_user') or self._play_context.remote_user
        if not tmp:
            tmp = self._make_tmp_path(remote_user)

        # skip if creates= is added to the module and the destination file already exists
        if creates:
            result = self._execute_module(module_name='stat', module_args=dict(path=creates), task_vars=task_vars)
            stat = result.get('stat', None)

            if stat and stat.get('exists', False):
                result['skipped'] = True
                result['msg'] = "skipped, since %s exists" % creates
                return result

        crt = os.path.expanduser(crt)

        # copy files
        if copy:
            source = self._loader.path_dwim_relative(self._loader.get_basedir(), 'files', crt)

            dest = tmp + os.path.basename(source)
            self._connection.put_file(source, dest)

            if self._play_context.become and self._play_context.become_user != 'root':
                if not self._play_context.check_mode:
                    self._remote_chmod('a+r', dest)


            new_module_args = self._task.args.copy()
            new_module_args.update(
                dict(
                    crt=dest,
                ),
            )

        else:
            new_module_args = self._task.args.copy()

        # run keystore module
        result.update(self._execute_module(module_args=new_module_args, task_vars=task_vars))
        return result
