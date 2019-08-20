from multiprocessing import Process, Queue
from scraper_factory.core import utils
from scraper_factory.core.scraper.scrapy import run_spider
from scraper_factory.core.spidermanager import SpiderManager
from scraper_factory.core.exceptions import SpiderNotFoundError


def scrape(spider_name, url):
    m = SpiderManager()
    spider_cls = m.instance(spider_name)

    if not spider_cls:
        msg = 'Spider {} doesn\'t exist'.format(spider_name)
        raise SpiderNotFoundError(msg)

    data_q = Queue()
    err_q = Queue()

    p = Process(target=run_spider, args=(spider_cls, url, data_q, err_q))
    p.start()
    p.join()

    if not err_q.empty():
        raise err_q.get()

    return utils.queue_to_list(data_q)


def list():
    m = SpiderManager()
    return m.get_spiders()
