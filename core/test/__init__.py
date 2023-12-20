# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       guxu
   date：          12/19/23
-------------------------------------------------
   Change Activity:
                   12/19/23:
-------------------------------------------------
"""
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "src"
)
sys.path.append(SOURCE_PATH)