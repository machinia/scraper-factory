from scraper_factory.core.base_spider import BaseSpider


class ValidMetadataSpider(BaseSpider):
    metadata = {
            'name': 'validmetadata',
            'version': '0.1',
            'description': 'this spider has all the metadata',
            'parameters': [{'param': 'bla'}]
    }

    def __init__(self, uri, queue, **kwargs):
        super().__init__('validmetadata', uri, queue, **kwargs)

    def parse(self, response):
        pass
