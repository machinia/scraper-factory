from unittest import TestCase
from tests.utils import read_from_file
from scraper_factory.core.api import scrape


class SpiderTestBase(TestCase):

    def verify_url_results(self, spider, url, results_file, detailed=False):
        results = scrape(spider, url=url, detailed=detailed)
        correct_results = read_from_file.read_results_from_file(results_file)

        self.assertEqual(len(list(results)), len(correct_results))

        for (test_result, proper_result) in zip(results, correct_results):
            # when items are no longer available on Amazon they don't have
            # price anymore and it's expected that eventually, the proper
            # result price will be 'None' so they all have been set
            # accordingly but if the item does have a price, only its first
            # character will be compared with the expected '$' one
            price = test_result['price']
            if price is not None:
                test_result['price'] = price[0]
                proper_result['price'] = '$'
            self.assertDictEqual(test_result, proper_result)
