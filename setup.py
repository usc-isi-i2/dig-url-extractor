# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 14:01:47
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-30 23:31:21


from distutils.core import setup
from setuptools import Extension,find_packages
from os import path

setup(
    name = 'digURLExtractor',
    version = '0.1.0',
    description = 'digURLExtractor',
    author = 'Lingzhe Teng',
    author_email = 'zwein27@gmail.com',
    url = 'https://github.com/ZwEin27/dig-url-extractor',
    download_url = 'https://github.com/ZwEin27/dig-url-extractor',
    packages = find_packages(),
    keywords = ['url', 'extractor'],
    install_requires=['digSparkUtil', 'digExtractor', 'esmre', 'idna', 'tldextract']
)