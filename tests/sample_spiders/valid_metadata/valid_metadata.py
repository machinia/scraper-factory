from scraper_factory.core.base_spider import BaseSpider


class ValidMetadataSpider(BaseSpider):
    metadata = {
            'name': 'valid_metadata',
            'version': '0.1',
            'description': 'this spider has all the metadata',
            'parameters': [{'param': 'bla'}]
    }

    def __init__(self, url, queue, detailed=False, **kwargs):
        super().__init__('valid_metadata', url, queue, **kwargs)

    def parse(self, response):
        pass
