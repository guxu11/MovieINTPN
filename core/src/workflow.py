# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     workflow.py
   Description :  execute the job with command line
   Author :       guxu
   date：          12/18/23
-------------------------------------------------
   Change Activity:
                   12/18/23:
-------------------------------------------------
"""
import argparse

def workflow(args):
    pass
    # 1. extract .srt file

    # 2. translate .srt file (optional)

    # 3. convert (optional) and concatenate video with caption


parser = argparse.ArgumentParser(prog="MovieINTPN", description="Movie Caption")

parser.add_argument("-t", "--test", default=100)

args = parser.parse_args()

print(args.test)