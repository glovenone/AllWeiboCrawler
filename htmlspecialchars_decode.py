#!/usr/bin/env python
#coding=utf8

'''Author:glove
Date:2014.04.01'''

import re
try:
    from htmlentitydefs import entitydefs
except ImportError:  # Python 3
    from html.entities import entitydefs


def htmlspecialchars_decode_func(m, defs=entitydefs):
    try:
        return defs[m.group(1)]
    except KeyError:
        return m.group(0)  # use as is


def htmlspecialchars_decode(string):
    pattern = re.compile("&(\w+?);")
    return pattern.sub(htmlspecialchars_decode_func, string)

