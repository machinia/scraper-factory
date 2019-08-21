from scrapy import Request
from scraper_factory.core.utils import remove_query_string
from scraper_factory.core.base_spider import BaseSpider


class AmazonWishlistSpider(BaseSpider):
    metadata = {
        'name': 'amazon-wishlist',
        'version': '0.1.0',
        'description': 'Scrapes an amazon wishlist and returns all '
                       'items in json format',
        'parameters': [
            {
                'name': 'url',
                'type': 'str',
                'default': None,
                'required': True,
                'description': 'Amazon wishlist url to be scraped'
            }, {
                'name': 'detailed',
                'type': 'bool',
                'default': False,
                'required': False,
                'description': 'Get detailed info of each item'
            }
        ]
    }

    def __init__(self, url, queue, detailed=False, **kwargs):
        super().__init__(self.metadata['name'], url, queue, **kwargs)
        self.__detailed = detailed

    def __get_sold_by(self, sold_by_list):
        sold_by = ''
        for el in sold_by_list:
            el = el.strip()
            if any([k in el for k in ('execute', 'function')]):
                continue
            if el == '.':
                sold_by = sold_by[:-1] + '.'
                break
            sold_by += el + ' '
        return sold_by.rstrip()

    def __get_prices(self, prices_list):
        list_price = None
        discount = None
        for el in prices_list:
            if el[0] == '$':
                list_price = el.strip()
            if el.find('$') > 0:
                discount = el[el.find('$'):].strip()
        return list_price, discount

    def __parse_item(self, response, obj={}):
        stock = response.css('#availability').css('span::text').extract_first()
        sold_by_list = response.css('#merchant-info *::text').extract()
        sold_by = self.__get_sold_by(sold_by_list)
        prices_list = response.css('#buyBoxInner') \
            .css('span.a-color-secondary::text').extract()
        list_price, discount = self.__get_prices(prices_list)

        obj['stock'] = stock.strip() if stock else None
        obj['sold_by'] = sold_by if sold_by else None
        obj['list_price'] = list_price
        obj['discount'] = discount
        self.q.put(obj)
        yield obj

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
            byline = item.css('#item-byline-' + id + '::text').extract_first()
            price = item.css('#itemPrice_' + id).css('span::text')\
                .extract_first()

            obj = {
                'id': id,
                'title': title,
                'byline': byline,
                'price': price,
                'link': remove_query_string(link),
                'img': remove_query_string(img)
            }

            # if detailed is True, scrapes each
            # wishlist item web page to get detailed info
            if self.__detailed:
                yield Request(link,
                              callback=self.__parse_item,
                              cb_kwargs={'obj': obj})
            else:
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
