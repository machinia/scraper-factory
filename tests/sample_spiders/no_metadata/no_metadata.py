from scraper_factory.core.base_spider import BaseSpider


class NoMetadataSpider(BaseSpider):

    def __init__(self, url, queue, detailed=False, **kwargs):
        super().__init__('no_metadata', url, queue, **kwargs)

    def parse(self, response):
        pass
