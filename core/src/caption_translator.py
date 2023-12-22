# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     caption_translator.py
   Description :  translate subtitle file
   Author :       guxu
   date：          12/19/23
-------------------------------------------------
   Change Activity:
                   12/19/23:
-------------------------------------------------
"""
import os.path
import time

from core.src.constants import *
from core.src.utils import _gen_default_trans_dst_path
import requests


class CaptionTranslator():
    def __init__(self, trans_src="google_translate"):
        if trans_src == "google_translate":
            self.url = "https://translate.googleapis.com/translate_a/single?" + \
                       "client=gtx" + \
                       "&sl={}" + \
                       "&tl={}" + \
                       "&dt=t&q={}"
        self.header = HEADER

    def translate(self, src_lang, dst_lang, sentence):
        url = self.url.format(src_lang, dst_lang, sentence)
        resp = requests.get(url, self.header)
        return self._parse_resp(resp)

    def translate_subtitle_file(self, src_lang, dst_lang, src_path, dst_path="na", keep_src=False):
        if dst_path == "na":
            dst_path = _gen_default_trans_dst_path(src_path, src_lang, dst_lang)
        if os.path.exists(dst_path):
            os.remove(dst_path)
        try:
            print("Start translating caption file from {} to {}".format(src_lang, dst_lang))
            with open(src_path, 'r') as r:
                with open(dst_path, 'w') as w:
                    line_no = 0
                    line = r.readline()
                    while line:
                        if (line_no - 2) % 4 == 0:
                            trans = self.translate(src_lang, dst_lang, line)
                            line = line + trans if keep_src else trans
                            time.sleep(0.1)
                        print(line)
                        w.write(line)
                        line = r.readline()
                        line_no += 1
            return dst_path
        except Exception as e:
            print(e)

    def _parse_resp(self, resp):
        result = ''
        try:
            json_array = resp.json()[0]
            for item in json_array:
                if item is not None:
                    result += item[0].strip()
        except Exception as e:
            print(e)
        return result.strip()


if __name__ == '__main__':
    c = CaptionTranslator()
    # resp = c.translate("us", "zh-CN", "are you ok")
    c.translate_subtitle_file("us", "zh-CN", "/Users/guxu/Movies/playground/normal_playground/demo.srt", keep_src=True)
    # print(resp)