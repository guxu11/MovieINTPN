# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     aug_parser
   Description :
   Author :       guxu
   date：          12/18/23
-------------------------------------------------
   Change Activity:
                   12/18/23:
-------------------------------------------------
"""
import argparse

parser = argparse.ArgumentParser(prog="MovieINTPN", description="Movie Caption")

parser.add_argument("-t", "--test", default=100)

args = parser.parse_args()

print(args.test)