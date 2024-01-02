# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     caption_concater
   Description :
   Author :       guxu
   date：          12/20/23
-------------------------------------------------
   Change Activity:
                   12/20/23:
-------------------------------------------------
"""
import os.path

from core.utils import _gen_default_concat_dst_path, _gen_default_convert_type_dst_path, _get_video_type, _reformat_name_with_space
from core.cmd_executor import CommandLineExec, ReturnCode


class CaptionConcater:
    def __init__(self):
        self.unsupported_type = {'ts', 'webm'}

    def ffmpeg_concat(self, video_path, caption_path, lang, output_path="na"):
        video_path = _reformat_name_with_space(video_path)
        if output_path == "na":
            output_path = _gen_default_concat_dst_path(video_path, lang)
        src_type = _get_video_type(video_path)
        if src_type in self.unsupported_type:
            print("Cannot concat caption to .{} file".format(src_type))
            print("Start converting to .mp4...")
            convert_video_path = _gen_default_convert_type_dst_path(video_path)
            rc = self._convert_type_no_loss(video_path, convert_video_path)
            video_path = convert_video_path
            output_path = _gen_default_convert_type_dst_path(output_path)
            if rc == ReturnCode.SUCCESS:
                print("Convert done!")
            else:
                raise Exception("Convert failed...")
        cmd = "ffmpeg -i {} -i {} -c:s mov_text -c:v copy -c:a copy {}".format(video_path, caption_path, output_path)
        print("Start concating...")
        print("concat command: {}".format(cmd))
        rc = CommandLineExec.exec_sync(cmd)
        if rc == ReturnCode.SUCCESS:
            print("Concat done!")
            if src_type in self.unsupported_type and os.path.exists(video_path):
                os.remove(video_path)
        else:
            raise Exception("Concat failed...")

    def _convert_type_no_loss(self, i_path, o_path):
        cmd = "ffmpeg -i {} -q:v 1 {}".format(i_path, o_path)
        print("converting command: {}".format(cmd))
        rc = CommandLineExec.exec_sync(cmd)
        return rc

if __name__ == '__main__':
    c = CaptionConcater()
    c.ffmpeg_concat(
        "/Users/guxu/Movies/playground/normal_playground/demo.webm",
        "/Users/guxu/Movies/playground/normal_playground/demo.srt",
        "en"
    )