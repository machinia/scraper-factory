from tests.utils.SpiderTestBase import SpiderTestBase


class AmazonWishlistSpiderTest(SpiderTestBase):

    def test_parse_no_scrolling(self):
        """
        Test response of AmazonWishlistSpider for a page
        that doesn't requiere scrolling
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
