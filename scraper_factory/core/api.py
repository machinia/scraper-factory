from multiprocessing import Process, Queue
from scraper_factory.core import utils
from scraper_factory.core.scraper.scrapy import run_spider
from scraper_factory.core.spidermanager import SpiderManager
from scraper_factory.core.exceptions import SpiderNotFoundError


def scrape(spider_name, **kwargs):
    m = SpiderManager()
    spider_cls = m.instance(spider_name)

    if not spider_cls:
        msg = 'Spider {} doesn\'t exist'.format(spider_name)
        raise SpiderNotFoundError(msg)

    err_q = Queue()
    data_q = Queue()
    kwargs['queue'] = data_q

    p = Process(target=run_spider,
                args=(spider_cls, err_q),
                kwargs=kwargs)
    p.start()
    p.join()

    if not err_q.empty():
        raise err_q.get()

    return utils.queue_to_list(data_q)


def spiders():
    m = SpiderManager()
    return m.get_spiders()
