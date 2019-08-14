from multiprocessing import Process, Queue
from scrapy import crawler
from scraper_factory.spiders.amazonwishlist import AmazonWishlistSpider
from scraper_factory.core import utils


def run_spider(url, queue):
    process = crawler.CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'LOG_LEVEL': 'ERROR',
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) '
                      'Gecko/20100101 Firefox/38.0'
    })
    process.crawl(AmazonWishlistSpider, url, queue)
    process.start()


def scrape(url):
    q = Queue()
    p = Process(target=run_spider, args=(url, q))
    p.start()
    p.join()
    return utils.queue_to_list(q)
