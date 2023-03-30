"""Kernel module"""
##!/usr/bin/env python
import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

workingdir = "/tmp/fortrankernel/"

class jansfortrankernel(Kernel):
    """The ipython Fortran kernel"""
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'fortran'
    language_version = '12.2.1'
    language_info = {
        'name': 'fortran',
        'mimetype': 'application/fortran',
        'file_extension': '.f90',
    }
    banner = "Fortran kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:            
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "proj.f90", "w") as f:
                    f.write(code)
            solution = pexpect.run('gfortran ' + workingdir  + 'proj.f90 -o runproj')
            if os.path.exists(workingdir+'runproj'):
                solution = pexpect.run(workingdir + 'runproj').decode('UTF-8')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        shutil.rmtree(workingdir)