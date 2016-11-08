import unittest

from digExtractor.extractor_processor import ExtractorProcessor
from digURLExtractor.url_extractor import URLExtractor


class TestURLExtractorMethods(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_url_extractor(self):
        doc = {
            'content': 'hello xixi https://www.todomasajes.net/b_k/flor/bk00.htm world', 'b': 'world'}

        extractor = URLExtractor().set_metadata({'extractor': 'url'})
        ep = ExtractorProcessor().set_input_fields(['content'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)
        updated_doc = ep.extract(doc)

        result = updated_doc['extracted'][0]['result']
        self.assertEqual(result[0]['value'],
                         'www.todomasajes.net/b_k/flor/bk00.htm')

    def test_url_extractor_context(self):
        doc = {
            'content': 'hello xixi https://www.todomasajes.net/b_k/flor/bk00.htm world', 'b': 'world'}

        extractor = URLExtractor().set_metadata({'extractor': 'url'})\
                                  .set_include_context(True)

        ep = ExtractorProcessor().set_input_fields(['content'])\
                                 .set_output_field('extracted')\
                                 .set_extractor(extractor)

        updated_doc = ep.extract(doc)

        result = updated_doc['extracted'][0]['result']
        self.assertEqual(result[0]['value'],
                         'www.todomasajes.net/b_k/flor/bk00.htm')
        self.assertEqual(result[0]['context']['start'],19)
        self.assertEqual(result[0]['context']['end'],56)


if __name__ == '__main__':
    unittest.main()
