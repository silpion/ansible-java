# TODO fix this

import os

from ansible import utils
from ansible import errors
from ansible.runner.return_data import ReturnData
import ansible.utils.template as template

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import pipes


class ActionModule(object):

    TRANSFER_FILES = True

    def __init__(self, runner):
        self.runner = runner

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwagrs):
        ''' handler for file transfer operations '''

        options = {}
        if complex_args:
            options.update(complex_args)
        options.update(utils.parse_kv(module_args))
        crt = options.get('crt', None)
        copy = utils.boolean(options.get('copy', 'yes'))
        creates = options.get('creates', None)

        if crt is None:
            result = dict(failed=True, msg="crt is required")
            return ReturnData(conn=conn, result=result)

        if creates:
            module_args_tmp = ""
            complex_args_tmp = dict(path=creates, get_md5=False, get_checksum=False)
            module_return = self.runner._execute_module(
                conn,
                tmp,
                'stat',
                module_args_tmp,
                inject=inject,
                complex_args=complex_args_tmp,
                persist_files=True
            )
            stat = module_return.result.get('stat', None)
            if stat and stat.get('exists', False):
                return ReturnData(
                    conn=conn,
                    comm_ok=True,
                    result=dict(
                        skipped=True,
                        changed=False,
                        msg=("skipped, since %s exists" % creates)
                    )
                )

        # TODO start fixing this here
        crt = self.runner._remote_expand_user(conn, crt, tmp)
        crt = template.template(self.runner.basedir, os.path.expanduser(crt), inject)
        if copy:
            if '_original_file' in inject:
                crt = utils.path_dwim_relative(inject['_original_file'], 'files', crt, self.runner.basedir)
            else:
                crt = utils.path_dwim(self.runner.basedir, crt)

        remote_checksum = self.runner._remote_checksum(conn, tmp, crt, inject)
        if remote_checksum == '4':
            result = dict(failed=True, msg="python isn't present on the system. Unable to compute checksum")
            return ReturnData(conn=conn, result=result)

        if copy:
            tmp_crt = tmp + 'crt'
            conn.put_file(crt, tmp_crt)

        if copy:
            if self.runner.sudo and self.runner.sudo_user != 'root' or self.runner.su and self.runner.su_user != 'root':
                if not self.runner.noop_on_check(inject):
                    self.runner._remote_chmod(conn, 'a+r', tmp_crt, tmp)

            new_module_args = dict(
                crt=tmp_crt,
            )

            if self.runner.noop_on_check(inject):
                new_module_args['CHECKMODE'] = True

            module_args = utils.merge_module_args(module_args, new_module_args)
        else:
            if self.runner.noop_on_check(inject):
                module_args += " CHECKMODE=True"

        return self.runner._execute_module(conn, tmp, 'keystore', module_args, inject=inject, complex_args=complex_args)
