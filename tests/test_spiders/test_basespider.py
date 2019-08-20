from multiprocessing import Queue
from scraper_factory.core.exceptions import InvalidUrlError
from tests.utils.spidertestbase import SpiderTestBase
from tests.sample_spiders.incomplete_metadata.incomplete_metadata \
    import IncompleteMetadataSpider
from tests.sample_spiders.no_metadata.no_metadata \
    import NoMetadataSpider
from tests.sample_spiders.valid_metadata.valid_metadata \
    import ValidMetadataSpider


class BaseSpiderTest(SpiderTestBase):

    def test_instance_params(self):
        """
        Test class attributes set on constructor
        """
        domain = 'https://'
        url = 'www.qwerty.com/dir/1234'
        base_url = 'www.qwerty.com'

        sp = ValidMetadataSpider(domain + url, Queue())
        self.assertEqual(sp.base_url, domain + base_url)
        self.assertEqual(sp.start_urls, [domain + url])
        self.assertEqual(len(sp.allowed_domains), 2)
        self.assertEqual(sp.allowed_domains, [base_url, url])

    def test_different_metadata(self):
        """
        Tests constructor when trying to instance spiders
        with incomplete metadata
        """
        url = 'https://www.sample.com'
        test_data = [
            (NoMetadataSpider, '"name" not defined in metadata'),
            (IncompleteMetadataSpider, '"version" not defined in metadata')
        ]

        for spider_cls, expected_stdout in test_data:
            with self.assertRaises(AttributeError) as err:
                spider_cls(url, Queue())
            self.assertEqual(expected_stdout, str(err.exception))

    def test_invalid_url(self):
        """
        Tests constructor behaviour trying to instance a spider
        with an invalid url
        """
        url = 'notaurl'
        self.assertRaises(InvalidUrlError, ValidMetadataSpider, url, Queue())
