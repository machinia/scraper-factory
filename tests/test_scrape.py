from unittest import TestCase
from scraper_factory.core.api import scrape
from scraper_factory.core import exceptions
from tests.utils import read_from_file


class TestScrape(TestCase):

    def test_invalid_path(self):
        """
        Test scrape method behaviour on a invalid spider path
        """
        name = 'non-existing-spider'
        url = 'https://www.amazon.com/hz/wishlist/ls/30E0MJEB97F1P'
        self.assertRaises(exceptions.SpiderNotFoundError,
                          scrape, name, url=url)

    def test_invalid_url(self):
        """
        Test scrape method when an invalid url is received
        """
        name = 'amazon-wishlist'
        url = 'notanurl'
        self.assertRaises(exceptions.InvalidUrlError, scrape, name, url=url)

    def test_valid_scrape(self):
        """
        Test happy path of the scrape method
        """
        name = 'amazon-wishlist'
        url = 'https://www.amazon.com/hz/wishlist/ls/30E0MJEB97F1P'
        results_file = 'amazon_wishlist_no_scrolling.txt'

        results = scrape(name, url=url)
        expected = read_from_file.read_results_from_file(results_file)

        self.assertEqual(len(list(results)), len(expected))
