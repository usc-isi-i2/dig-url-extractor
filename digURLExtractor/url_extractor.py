# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 22:33:42
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-10-02 15:41:50


import copy
from digExtractor.extractor import Extractor
from ze_url_extractor import ZEURLExtractor


class URLExtractor(Extractor):

    def __init__(self):
        self.renamed_input_fields = ['text']
        self.zeurl = ZEURLExtractor()

    def extract(self, doc):
        if 'text' in doc:
            return self.zeurl.extract(doc['text'],
                                      self.get_include_context())
        return None

    def get_metadata(self):
        return copy.copy(self.metadata)

    def set_metadata(self, metadata):
        self.metadata = metadata
        return self

    def get_renamed_input_fields(self):
        return self.renamed_input_fields
