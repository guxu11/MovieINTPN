# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     caption_converter
   Description :  extract subtitles
   Author :       guxu
   date：          12/19/23
-------------------------------------------------
   Change Activity:
                   12/19/23:
-------------------------------------------------
"""
import os

from core.cmd_executor import CommandLineExec
from core.utils import _gen_default_extract_dst_path, _reformat_name_with_space
from core.constants import LANGUAGE_CODES

"""
extractor subtitles using autosub command-line tool, which is not in high accuracy.
TODO: 1. Do more research on increasing the accuracy
      2. Recognize the language of input a/v source automatically
      3. user-friendly notifications during extracting
"""

class CaptionExtractor():
    def __init__(self):
        self.lang_map = LANGUAGE_CODES

    def extract(self, src_path, src_lang, dst_path='na', *args):
        src_path = _reformat_name_with_space(src_path)
        if dst_path == 'na':
            dst_path = _gen_default_extract_dst_path(src_path)
        cmd = "autosub -S {} -D {} {} -o {}".format(src_lang, src_lang, src_path, dst_path)
        print("Start extracting caption...")
        print("Extraction command: {}".format(cmd))
        ret_code = CommandLineExec.exec_sync(cmd)
        if ret_code == 0:
            return dst_path
        else:
            raise Exception("extract failed")


if __name__ == '__main__':
    c = CaptionExtractor()
    c.extract("/Users/guxu/Movies/playground/normal_playground/demo.webm", "en")
