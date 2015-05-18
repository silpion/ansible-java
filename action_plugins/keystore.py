# (c) 2015, Mark Kusch <mark.kusch@silpion.de>

import os

from ansible import utils
from ansible import errors
from ansible.runner.return_data import ReturnData


class ActionModule(object):

    TRANSFER_FILES = True

    def __init__(self, runner):
        self.runner = runner

    def run(self, conn, tmp, module_name, module_args, inject, complex_args=None, **kwargs):
        ''' handler for file transfer operations '''

        options = {}
        if complex_args:
            options.update(complex_args)
        options.update(utils.parse_kv(module_args))

        crt = options.get('crt', None)
        copy = utils.boolean(options.get('copy', 'yes'))
        creates = options.get('creates', None)


        # this module requires at least the crt= to be present
        if crt is None:
            result = dict(failed=True, msg="crt is required")
            return ReturnData(conn=conn, result=result)


        # skip if creates= is added to the module and the destination file already exists
        if creates:
            stat_module_args = ""
            stat_complex_args = dict(path=creates, get_md5=False, get_checksum=False)
            stat_module = self.runner._execute_module(
                conn,
                tmp,
                'stat',
                stat_module_args,
                complex_args=stat_complex_args,
                inject=inject,
                persist_files=True
            )
            stat = stat_module.result.get('stat', None)
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

        crt = utils.template.template(self.runner.basedir, os.path.expanduser(crt), inject)

        # copy files
        if copy:
            source = utils.path_dwim(self.runner.basedir, crt)
            dest = tmp + os.path.basename(crt)
            conn.put_file(source, dest)

            if self.runner.become and self.runner.become_user != 'root':
                if not self.runner.noop_on_check(inject):
                    self.runner._remote_chmod(conn, 'a+r', dest, tmp)

            new_module_args = dict(crt=dest)
            if self.runner.noop_on_check(inject):
                new_module_args['CHECKMODE'] = True

            module_args = utils.merge_module_args(module_args, new_module_args)
        else:
            if self.runner.noop_on_check(inject):
                module_args += " CHECKMODE=True"


        # run keystore module
        return self.runner._execute_module(conn, tmp, 'keystore', module_args, complex_args=complex_args, inject=inject)
