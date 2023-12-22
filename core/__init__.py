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
import argparse, sys
from core.constants import LANGUAGE_CODES
from core.caption_extractor import CaptionExtractor
from core.caption_translator import CaptionTranslator
from core.caption_concater import CaptionConcater

def workflow(args):
    src_path = args.input
    dst_path = args.output
    src_lang = args.input_language
    dst_lang = args.output_language
    retain_origin = args.retain_origin

    if dst_lang not in LANGUAGE_CODES:
        dst_lang = src_lang
    # 1. extract .srt file
    extractor = CaptionExtractor()
    caption_path = extractor.extract(src_path, src_lang)

    # 2. translate .srt file (optional)
    if src_lang != dst_lang:
        translator = CaptionTranslator()
        caption_path = translator.translate_subtitle_file(src_lang, dst_lang, caption_path, keep_src=retain_origin)

    # 3. convert (optional) and concatenate video with caption
    concater = CaptionConcater()
    dst_lang = dst_lang if not retain_origin or dst_lang == src_lang else "{}_{}".format(src_lang, dst_lang)
    concater.ffmpeg_concat(src_path, caption_path, dst_lang, dst_path)


def main():

    parser = argparse.ArgumentParser(prog="MovieINTPN", description="Movie Caption")
    parser.set_defaults(callback=workflow)
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, default="na")
    parser.add_argument("-il", "--input_language", type=str, required=True)
    parser.add_argument("-ol", "--output_language", type=str)
    parser.add_argument("-ro", "--retain_origin", action="store_true")

    args = parser.parse_args()
    args.callback(args)

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    main()
