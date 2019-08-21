from abc import ABC, abstractmethod
from urllib.parse import urlparse
from scrapy import Spider
from scraper_factory.core.utils import validate_url
from scraper_factory.core.exceptions import InvalidUrlError


class BaseSpider(ABC, Spider):
    __METADATA_KEYS = ('name', 'version', 'description', 'parameters')
    metadata = {}

    def __init__(self, name, uri, queue, **kwargs):
        if not validate_url(uri):
            raise InvalidUrlError('Invalid URL')

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

    @staticmethod
    def check_metadata(metadata):
        for key in BaseSpider.__METADATA_KEYS:
            if not metadata.get(key):
                msg = '"{}" not defined in metadata'.format(key)
                raise AttributeError(msg)
