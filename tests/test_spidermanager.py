import os
from unittest import TestCase
from scraper_factory.core.spidermanager import SpiderManager
from tests.sample_spiders.valid_metadata.valid_metadata \
    import ValidMetadataSpider


class TestSpiderManager(TestCase):

    @classmethod
    def tearDownClass(cls):
        if 'SPIDER_PATH' in os.environ:
            del os.environ['SPIDER_PATH']

    def test_invalid_path(self):
        """
        Tests an invalid path as parameter
        """
        path = '/invalidpath'
        os.environ['SPIDER_PATH'] = path
        self.assertRaises(AttributeError, SpiderManager)

    def test_several_folders(self):
        """
        Searches for spiders in several folders with
        valid and invalid spiders
        """
        spider_path = 'tests/sample_spiders/'
        test_data = [
            ('valid_metadata', 1),
            ('no_metadata', 0),
            ('incomplete_metadata', 0),
            ('two_spiders_one_file', 0),
            ('no_basespider_inheritance', 0)
        ]

        m = SpiderManager()
        for spidername, valid_spiders in test_data:
            path = spider_path + spidername
            os.environ['SPIDER_PATH'] = path

            m.load(path)
            spiders = m.get_spiders()

            self.assertEqual(type(spiders), list)
            self.assertEqual(len(spiders), valid_spiders)

    def test_manager_instances_success(self):
        """
        Tests return of instance method when requesting a loaded spider
        """
        spider_name = 'valid_metadata'
        path = 'tests/sample_spiders/' + spider_name
        os.environ['SPIDER_PATH'] = path

        m = SpiderManager()
        inst = m.instance(spider_name)
        self.assertEqual(inst.__name__, ValidMetadataSpider.__name__)

    def test_manager_instances_not_found(self):
        """
        Tests response when requesting the instance of a spider
        that isn't loaded
        """
        spider_name = 'no_metadata'
        path = 'tests/sample_spiders/' + spider_name
        os.environ['SPIDER_PATH'] = path

        m = SpiderManager()
        inst = m.instance(spider_name)
        self.assertEqual(inst, None)
