from scrapy import Request
from scraper_factory.core.utils import remove_query_string
from scraper_factory.core.base_spider import BaseSpider


class AmazonWishlistSpider(BaseSpider):

    def __init__(self, uri, queue, **kwargs):
        super().__init__('amazonwishlist', uri, queue, **kwargs)

    def parse(self, response):
        page_items = response.css('.g-item-sortable')

        for item in page_items:
            id = item.css('li::attr(data-itemid)').extract_first()
            title = item.css('#itemName_' + id + '::text').extract_first()
            link = item.css('#itemName_' + id + '::attr(href)')\
                .extract_first()
            if link:
                link = self.base_url + link
            img = item.css('#itemImage_' + id).css('img::attr(src)')\
                .extract_first()

            obj = {
                'id': id,
                'title': title,
                'link': remove_query_string(link),
                'img': remove_query_string(img)
            }

            self.q.put(obj)
            yield obj

        # manage "infinite scrolldown"
        has_next = response.css('#sort-by-price-next-batch-lek'
                                '::attr(value)').extract_first()
        if has_next:
            lek_uri = response.css(
                '#sort-by-price-load-more-items-url-next-batch::attr(value)')\
                .extract_first()
            next_page = self.base_url + lek_uri
            yield Request(next_page)
