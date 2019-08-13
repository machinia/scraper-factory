from tests.utils.spidertestbase import SpiderTestBase
from scraper_factory.spiders.amazonwishlist import AmazonWishlistSpider

from multiprocessing import Queue


class AmazonWishlistSpiderTest(SpiderTestBase):

    def test_parse_no_scrolling(self):
        """
        Test response of AmazonWishlistSpider for a page
        that doesn't require scrolling
        """
        url = 'https://www.amazon.com/hz/wishlist/ls/30E0MJEB97F1P'
        results_file = 'amazon_wishlist_no_scrolling.txt'
        self.verify_url_results(url, results_file)

    def test_parse_with_scrolling(self):
        """
        Test response of AmazonWishlistSpider for a page
        that requires scrolling
        """
        url = 'https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN'
        results_file = 'amazon_wishlist_with_scrolling.txt'
        self.verify_url_results(url, results_file)

    def test_any_url(self):
        """
        Test response of AmazonWishlistSpider for a page
        that isn't a amazon wishlist
        """
        url = 'https://www.amazon.com/'
        results_file = 'amazon_wishlist_any_url.txt'
        self.verify_url_results(url, results_file)

    def test_invalid_url(self):
        """
        Test response of AmazonWishlistSpider for a page
        that isn't a amazon wishlist
        """
        url = 'not_an_url'
        results_file = 'amazon_wishlist_any_url.txt'
        self.verify_url_results(url, results_file)

    def test_instance_params(self):
        """
        Test object parameters that set when instancing
        """
        domain = 'https://'
        url = 'www.amazon.com/hz/wishlist/ls/24XY9873RPAYN'
        base_url = 'www.amazon.com'

        sp = AmazonWishlistSpider(domain + url, Queue())
        self.assertEqual(sp.base_url, domain + base_url)
        self.assertEqual(sp.start_urls, [domain + url])
        self.assertEqual(len(sp.allowed_domains), 2)
        self.assertEqual(sp.allowed_domains, [base_url, url])
