from scraper_factory.core.base_spider import BaseSpider


class NoMetadataSpider(BaseSpider):

    def __init__(self, uri, queue, **kwargs):
        super().__init__('no_metadata', uri, queue, **kwargs)

    def parse(self, response):
        pass
