class NotFromBaseSpider(object):
    metadata = {
            'name': 'first-spider',
            'version': '0.1.0',
            'description': 'first spider in file',
            'parameters': [{'param': 'bla'}]
    }

    def __init__(self, uri, queue, **kwargs):
        pass

    def parse(self, response):
        pass
