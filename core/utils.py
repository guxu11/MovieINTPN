# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       guxu
   date：          12/20/23
-------------------------------------------------
   Change Activity:
                   12/20/23:
-------------------------------------------------
"""
import os.path
from core.constants import SPECIAL_SIGN


def _gen_default_extract_dst_path(src_path):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + "/"
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + ".srt"
    dst_path = prefix + dst_file_name if prefix != '/' else dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _gen_default_trans_dst_path(src_path, src_lang, dst_lang, keep_src=False):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1])
    if not keep_src:
        dst_file_name += "_{}.srt".format(dst_lang)
    else:
        dst_file_name += "{}_{}.srt".format(src_lang, dst_lang)
    dst_path = prefix + dst_file_name if prefix != "/" else dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _gen_default_concat_dst_path(src_path, lang):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + "_{}.{}".format(lang, name_components[-1])
    dst_path = prefix + dst_file_name if prefix != "/" else dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _get_video_type(src_path):
    return src_path.split('.')[-1]


def _gen_default_convert_type_dst_path(src_path):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + ".mp4"
    dst_path = prefix + dst_file_name if prefix != "/" else dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _add_suffix_if_exist(src_path):
    while os.path.exists(src_path):
        components = src_path.split('.')
        src_path = ".".join(components[:-1]) + "-1." + components[-1]
    return src_path


def _reformat_name_with_space(src_path):
    formatted = ''
    for i, c in enumerate(src_path):
        if i > 0 and c in SPECIAL_SIGN and src_path[i - 1] != '\\':
            formatted += '\\'
        formatted += c
    return formatted


def _deformat_name_with_space(src_path):
    for sign in SPECIAL_SIGN:
        src_path.replace("\\{}".format(sign), sign)
    return src_path


if __name__ == '__main__':
    print(_deformat_name_with_space("/Users/demo\' 123\\ .ts"))
