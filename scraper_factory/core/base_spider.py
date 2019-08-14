from abc import ABC, abstractmethod
from urllib.parse import urlparse
from scrapy import Spider
from scraper_factory.core.utils import validate_url


class BaseSpider(ABC, Spider):

    def __init__(self, name, uri, queue, **kwargs):
        if not validate_url(uri):
            raise ValueError('Invalid URL')

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
