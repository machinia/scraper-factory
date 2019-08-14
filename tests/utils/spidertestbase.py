from unittest import TestCase
from tests.utils import read_from_file
from scraper_factory.core.scrape import scrape


class SpiderTestBase(TestCase):

    def verify_url_results(self, url, results_file):
        results = scrape(url)
        correct_results = read_from_file.read_results_from_file(results_file)

        self.assertEqual(len(list(results)), len(correct_results))

        for (test_result, proper_result) in zip(results, correct_results):
            self.assertDictEqual(test_result, proper_result)
