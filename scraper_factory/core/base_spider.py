from abc import ABC, abstractmethod
from urllib.parse import urlparse
from scrapy import Spider
from scraper_factory.core.utils import validate_url


class BaseSpider(ABC, Spider):
    metadata = {
            'name': None,
            'version': None,
            'description': None,
            'parameters': None
    }

    def __init__(self, name, uri, queue, **kwargs):
        if not validate_url(uri):
            raise ValueError('Invalid URL')

        self.check_metadata(self.metadata)

        self.name = name
        parsed_url = urlparse(uri)
        self.start_urls = [uri]
        self.base_url = parsed_url.scheme + '://' + parsed_url.netloc
        self.allowed_domains = []
        self.allowed_domains.append(parsed_url.netloc)
        self.allowed_domains.append(uri.split('//')[-1])

        self.q = queue
        super().__init__(**kwargs)

    @abstractmethod
    def parse(self, response):
        """This method should implement how to parse the
         response data."""
        pass

    @classmethod
    def check_metadata(cls, metadata):
        for key in cls.metadata:
            if not metadata.get(key):
                msg = '"{}" not defined in metadata'.format(key)
                raise AttributeError(msg)
