from scraper_factory.core.base_spider import BaseSpider


class IncompleteMetadataSpider(BaseSpider):
    metadata = {
            'name': 'incompletemetadata',
            'description': 'this spider has missing parameters',
    }

    def __init__(self, uri, queue, **kwargs):
        super().__init__('incompletemetadata', uri, queue, **kwargs)

    def parse(self, response):
        pass
