# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     commandLineExec
   Description :
   Author :       guxu
   date：          12/19/23
-------------------------------------------------
   Change Activity:
                   12/19/23:
-------------------------------------------------
"""
import os
import subprocess


class ReturnCode:
    UNKNOWN = -100
    SUCCESS = 0
    FAIL = -1

class CommandLineExec():
    @staticmethod
    def exec_sync(cmd, cwd=os.getcwd()):
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                check=True,
                cwd=cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return_code = result.returncode
            print("Output:\n", result.stdout.decode('utf-8'))
        except Exception as e:
            return_code = ReturnCode.FAIL
            print("Error:\n", e)

        return return_code