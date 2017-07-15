#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author: xiaoyizong <yizongxiao>
# @Date:   15-07-2017 13:02:40
# @Email:  xiaoyizong@baidu.com
# @Filename: types.py
# @Last modified by:   yizongxiao
# @Last modified time: 15-07-2017 13:11:20
# @Copyright: Baidu.inc

import sys
import ast

boolean = str

if sys.version_info > (3,):
    long = int
    unicode = str
    str = bytes


def convert(value, type):
    """ Convert / Cast function """
    if issubclass(type, str) and not (value.upper() in ['FALSE', 'TRUE']):
        return value.decode('utf-8')
    elif issubclass(type, unicode):
        return unicode(value)
    elif issubclass(type, int):
        return int(value)
    elif issubclass(type, long):
        return long(value)
    elif issubclass(type, float):
        return float(value)
    elif issubclass(type, boolean) and (value.upper() in ['FALSE', 'TRUE']):
        if str(value).upper() == 'TRUE':
            return True
        elif str(value).upper() == 'FALSE':
            return False
    else:
        try:
            return ast.literal_eval(str(value).decode('utf-8'))
        except:
            return value
