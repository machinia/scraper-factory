from scraper_factory.core.base_spider import BaseSpider


class FirstSpider(BaseSpider):
    metadata = {
            'name': 'first-spider',
            'version': '0.1.0',
            'description': 'first spider in file',
            'parameters': [{'param': 'bla'}]
    }

    def __init__(self, url, queue, detailed=False, **kwargs):
        pass

    def parse(self, response):
        pass


class SecondSpider(BaseSpider):
    metadata = {
            'name': 'second-spider',
            'version': '0.1.0',
            'description': 'second spider in file',
            'parameters': [{'param': 'bla'}]
    }

    def __init__(self, url, queue, detailed=False, **kwargs):
        pass

    def parse(self, response):
        pass
