# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     unittest
   Description :
   Author :       guxu
   date：          12/19/23
-------------------------------------------------
   Change Activity:
                   12/19/23:
-------------------------------------------------
"""
import os

from core.src.cmd_executor import CommandLineExec

def test_cmd_sync_non_param():
    cmd = "ls -a"
    rc = CommandLineExec.exec_sync(cmd)
    print(rc)

def test_cmd_sync_with_param():
    cmd = "ls -a"
    cwd = os.path.join(os.getcwd(), 'core/src')
    rc = CommandLineExec.exec_sync(cmd, cwd)
    print(rc)

if __name__ == '__main__':
    test_cmd_sync_with_param()