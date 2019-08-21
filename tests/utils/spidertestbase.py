from unittest import TestCase
from tests.utils import read_from_file
from scraper_factory.core.api import scrape


class SpiderTestBase(TestCase):

    def verify_url_results(self, spider, url, results_file, detailed=False):
        results = scrape(spider, url=url, detailed=detailed)
        correct_results = read_from_file.read_results_from_file(results_file)

        self.assertEqual(len(list(results)), len(correct_results))

        sorted_results = []
        for item in results:
            id = item['id']
            for i in range(len(correct_results)):
                if correct_results[i]['id'] != id:
                    continue
                sorted_results.append(correct_results[i])
                correct_results.pop(i)
                break

        for (test_result, proper_result) in zip(results, sorted_results):
            # when items are no longer available on Amazon they don't have
            # price anymore and it's expected that eventually, the proper
            # result price will be 'None' so they all have been set
            # accordingly but if the item does have a price, only its first
            # character will be compared with the expected '$' one
            for key in ('price', 'list_price', 'discount'):
                value = test_result.get(key)
                if value is not None:
                    test_result[key] = value[0]
                    proper_result[key] = '$'

            for key in ('sold_by', 'stock'):
                value = test_result.get(key)
                if value is not None:
                    test_result[key] = None

            self.assertDictEqual(test_result, proper_result)
