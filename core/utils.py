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


def _gen_default_extract_dst_path(src_path):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + ".srt"
    dst_path = prefix + dst_file_name
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
    dst_path = prefix + dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _gen_default_concat_dst_path(src_path, lang):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + "_{}.{}".format(lang, name_components[-1])
    dst_path = prefix + dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _get_video_type(src_path):
    return src_path.split('.')[-1]


def _gen_default_convert_type_dst_path(src_path):
    components = src_path.split('/')
    prefix = "/".join(components[:-1]) + '/'
    file_name = components[-1]
    name_components = file_name.split('.')
    dst_file_name = '.'.join(name_components[:-1]) + ".mp4"
    dst_path = prefix + dst_file_name
    return dst_path if not os.path.exists(dst_path) else _add_suffix_if_exist(dst_path)


def _add_suffix_if_exist(src_path):
    while os.path.exists(src_path):
        components = src_path.split('.')
        src_path = ".".join(components[:-1]) + "-1." + components[-1]
    return src_path
