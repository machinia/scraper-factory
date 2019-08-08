from scraper_factory.core import utils

from unittest import TestCase
from multiprocessing import Queue
from time import sleep


class TestCoreUtils(TestCase):

    def test_empty_list_to_queue(self):
        """
        Test queue_to_list method with an empty queue
        """
        q = Queue()
        lst = []

        r = utils.queue_to_list(q)
        self.assertEqual(r, lst)

    def test_list_to_queue(self):
        """
        Test queue_to_list with a queue with values
        :return:
        """
        q = Queue()
        lst = ['a', 1, {'key': 'value'}, None, list()]

        for i in lst:
            q.put(i)
            sleep(0.01)

        r = utils.queue_to_list(q)
        self.assertEqual(lst, r)

    def test_exception_on_list_to_queue(self):
        """
        Test queue_to_list using different type of arguments
        :return:
        """
        q = [None, list(), 1, "qwerty", {}]
        for i in q:
            self.assertRaises(TypeError, utils.queue_to_list, i)

    def test_remove_query_string(self):
        """
        Test remove_query_string with several inputs
        """
        url_list = [
            ('', ''),
            ('amazon', 'amazon'),
            ('amazon.com', 'amazon.com')
            ('https://www.amazon.com', 'https://www.amazon.com'),
            ('https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN/ref=cm_go',
             'https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN/ref=cm_go'),
            ('https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN?'
             'filter=DEFAULT&viewType=list&lek=97df910a-49ea-9a85-c1511c756f36',
             'https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN')
        ]

        for test_url, expected_url in url_list:
            self.assertEqual(expected_url, utils.remove_query_string(test_url))

    def test_exception_remove_query_string(self):
        """
        Test remove_query_string using different type of arguments
        """
        arg = [None, list(), 1, {}]
        for a in arg:
            self.assertRaises(TypeError, utils.remove_query_string, a)
