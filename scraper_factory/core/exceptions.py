class ScraperFactoryException(Exception):
    pass


class SpiderNotFoundError(ScraperFactoryException):
    pass


class InvalidUrlError(ScraperFactoryException):
    pass
