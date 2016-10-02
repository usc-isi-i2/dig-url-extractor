# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-26 13:48:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-02 15:05:12

"""
Inspired by imranghory's urlextractor at https://github.com/imranghory/urlextractor

"""

import re
import os
import sys

# Regular expression accelerator
# Modules used to accelerate execution of a large collection of regular expressions using the Aho-Corasick algorithms.
import esm

# Internationalized Domain Names in Applications (IDNA)
# https://pypi.python.org/pypi/idna
import idna 

# Accurately separate the TLD from the registered domain and subdomains of a URL, using the Public Suffix List.
# https://github.com/john-kurkowski/tldextract
import tldextract

######################################################################
#   Constant
######################################################################

######################################################################
#   Regular Expression
######################################################################

# preprocess
re_dot = re.compile(r'(?:\s+?dot\s+?)', re.IGNORECASE)

# query
reg_url_charactor = '[a-z0-9-.]'

re_url_charactor = re.compile(reg_url_charactor, re.IGNORECASE)
re_pretld = re.compile(reg_url_charactor+'+?$', re.IGNORECASE)
re_posttld = re.compile(':?[0-9]*[/[!#$&-;=?a-z_]+]?', re.IGNORECASE)

######################################################################
#   Main Scripts
######################################################################

class ZEURLExtractor(object):

    def __init_tld_index():
        tldindex = esm.Index()
        tlds = (tldextract.TLDExtract()._get_tld_extractor().tlds)
        ldindex = esm.Index()
        for tld in tlds:
            tldindex.enter('.' + tld.encode('idna'))
        tldindex.fix()
        return tldindex
    
    tldindex = __init_tld_index()

    @staticmethod
    def preprocess(text):

        def clean(text):
            text = re_dot.sub('.', text)
            return text

        text = clean(text)
        return text

    @staticmethod
    def query(text):
        ans = []
        exts = ZEURLExtractor.tldindex.query(text)
        for ext in exts:
            pretld, posttld = None, None
            url = ''
            tld = ext[1]
            startpt, endpt = ext[0][0], ext[0][1]
            if len(text) > endpt:
                nextcharacter = text[endpt]
                if re_url_charactor.match(nextcharacter):
                    continue
                posttld = re_posttld.match(text[endpt:])
            pretld = re_pretld.search(text[:startpt])
            if pretld:
                url = pretld.group(0)
                startpt -= len(pretld.group(0))
            url += tld
            if posttld:
                url += posttld.group(0)     
                endpt += len(posttld.group(0))
            url = url.rstrip(',.') 
            ans.append(url)
        ans = list(set([_ for _ in ans if _]))
        return ans

    @staticmethod
    def extract(text):
        text = text.encode('ascii', 'ignore')
        text= ZEURLExtractor.preprocess(text)
        ans = ZEURLExtractor.query(text)
        return ans
