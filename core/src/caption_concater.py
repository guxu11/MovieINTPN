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
from core.src.utils import _gen_default_concat_dst_path, _gen_default_convert_type_dst_path, _get_video_type
from core.src.cmd_executor import CommandLineExec, ReturnCode

class CaptionConcater:
    def __init__(self):
        self.unsupport_type = {'ts', 'webm'}

    def ffmpeg_concat(self, video_path, caption_path, lang, output_path="na"):
        if output_path == "na":
            output_path = _gen_default_concat_dst_path(video_path, lang)
        src_type = _get_video_type(video_path)
        if src_type in self.unsupport_type:
            print("Cannot concat caption to .{} file".format(src_type))
            print("Start converting to .mp4...")
            o_convert_path = _gen_default_convert_type_dst_path(video_path)
            rc = self._convert_type_no_loss(video_path, o_convert_path)
            if rc == ReturnCode.SUCCESS:
                print("Convert done!")
            else:
                raise Exception("Convert failed...")
        cmd = "ffmpeg -i {} -i {} -c:s mov_text -c:v copy -c:a copy {}".format(video_path, caption_path, output_path)
        print("Start concating")
        rc = CommandLineExec.exec_sync(cmd)
        if rc == ReturnCode.SUCCESS:
            print("Concat done!")
        else:
            raise Exception("Concat failed...")


    def _convert_type_no_loss(self, i_path, o_path):
        cmd = "ffmpeg -i {} -q:v 1 {}".format(i_path, o_path)
        rc = CommandLineExec.exec_sync(cmd)
        return rc