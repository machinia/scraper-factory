from tests.utils.SpiderTestBase import SpiderTestBase


class AmazonWishlistSpiderTest(SpiderTestBase):

    def test_parse_no_scrolling(self):
        url = 'https://www.amazon.com/hz/wishlist/ls/30E0MJEB97F1P'
        results_file = 'amazon_wishlist_no_scrolling.txt'
        self.verify_url_results(url, results_file)

    def test_parse_with_scrolling(self):
        url = 'https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN'
        results_file = 'amazon_wishlist_with_scrolling.txt'
        self.verify_url_results(url, results_file)
