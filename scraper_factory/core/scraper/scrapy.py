import os
import sys
from scrapy import crawler
from scrapy.settings import Settings


def get_settings():
    """
    Get settings from the 'scrapy_settings.py' file
    :return: scrapy.settings.Settings instance object
    """
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    settings = Settings()
    settings.setmodule('scrapy_settings', priority='project')
    return settings


def err_callback(failure, err_q):
    """
    Error callback, called upon errors on crawler
    :param failure: twisted.Failure object
    :param err_q: queue where errors are handed to parent process
    :return: Nothing
    """
    err_q.put(failure.value)


def run_spider(spider_cls, err_queue, **kwargs):
    """
    Scrapes a url with the given spider class
    :param spider_cls: spider constructor to be used
    :param url: string with the url to scrape
    :param data_queue: multiprocessing Queue where data will be stored
    :param err_queue: multiprocessing Queue where errors will be stored
    :return: Nothing
    """
    process = crawler.CrawlerProcess(settings=get_settings())
    p = process.crawl(crawler_or_spidercls=spider_cls, **kwargs)
    p.addErrback(err_callback, err_queue)
    process.start()
