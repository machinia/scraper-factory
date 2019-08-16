from multiprocessing import Process, Queue
from scrapy import crawler
from scraper_factory.core import utils
from scraper_factory.core.spidermanager import SpiderManager
from scraper_factory.core.exceptions import SpiderNotFoundError


def err_callback(failure, err_q):
    """
    Error callback, called upon errors on crawler
    :param failure: twisted.Failure object
    :param err_q: queue where errors are handed to parent process
    :return: Nothing
    """
    err_q.put(failure.value)


def run_spider(spider_cls, url, data_queue, err_queue):
    process = crawler.CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) '
                      'Gecko/20100101 Firefox/38.0'
    })
    p = process.crawl(spider_cls, uri=url, queue=data_queue)
    p.addErrback(err_callback, err_queue)
    process.start()


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
