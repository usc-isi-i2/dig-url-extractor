import sys
import time
import os
import unittest

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

from digExtractor.extractor import Extractor
from digExtractor.extractor_processor import ExtractorProcessor
from digURLExtractor.url_extractor import URLExtractor

class TestURLExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_url_extractor(self):
        doc = {'content': 'hello xixi https://www.todomasajes.net/b_k/flor/bk00.htm world', 'b': 'world'}

        extractor = URLExtractor().set_metadata({'extractor': 'url'})
        extractor_processor = ExtractorProcessor().set_input_fields(['content']).set_output_field('extracted').set_extractor(extractor)
        updated_doc = extractor_processor.extract(doc)
        self.assertEqual(updated_doc['extracted'][0]['value'], ['www.todomasajes.net/b_k/flor/bk00.htm'])

    

if __name__ == '__main__':
    unittest.main()



