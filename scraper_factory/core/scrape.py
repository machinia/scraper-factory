from scrapy.crawler import CrawlerProcess
from scraper_factory.spiders.amazonwishlist import AmazonWishlistSpider


def scrape(url):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'LOG_LEVEL': 'INFO'
    })

    scraped_data = []
    process.crawl(AmazonWishlistSpider, url, scraped_data)
    process.start()
    return scraped_data
