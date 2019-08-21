from scraper_factory.core.base_spider import BaseSpider


class IncompleteMetadataSpider(BaseSpider):
    metadata = {
            'name': 'incomplete_metadata',
            'description': 'this spider has missing parameters',
    }

    def __init__(self, url, queue, detailed=False, **kwargs):
        super().__init__('incomplete_metadata', url, queue, **kwargs)

    def parse(self, response):
        pass
