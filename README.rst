Scraping Factory
================

|travis| |coverage| |pypi| |pyversion|

Scraping library to retrieve data from useful pages, such as Amazon wishlists

API
---

The API to use the library, scrape data and manage spiders is the following:

- ``scrape(SPIDER_NAME, URL)``: scrapes the given ``URL`` using the spider referenced on ``SPIDER_NAME``.
- ``spiders()``: list all spiders found by the library.


Custom Spiders
--------------

Using custom spiders is possible, as long as they:

- They must be implemented as a class, and inherit from ``BaseSpider``.

- The spider file need to be either on ``scraper_factory/spiders``, or in a custom location, as long as the environment variable ``$SPIDER_PATH`` is set to the directory where the spider is located.

Usage example
-------------

.. code-block:: python

    >>> import scraper_factory as SF
    >>> SF.scrape('amazon-wishlist', 'https://www.amazon.com/hz/wishlist/ls/24XY9873RPAYN')
    [{
    	'id': 'I1MZVK8RDPYK8P',
    	'title': 'AmazonBasics Heavy Weight Ruled Lined Index Cards, White, 3x5 Inch Card, 100-Count - AMZ63500',
    	'byline': None,
    	'price': None,
    	'link': 'https://www.amazon.com/dp/B06XSRLP51/',
    	'img': 'https://images-na.ssl-images-amazon.com/images/I/71i7LVTzpsL._SS135_.jpg'
    }, {
    	'id': 'I14TUJ6TADACU5',
    	'title': "Women's Walking Shoes Sock Sneakers - Mesh Slip On Air Cushion Lady Girls Modern Jazz Dance Easy Shoes Platform Loafers",
    	'byline': None,
    	'price': None,
    	'link': 'https://www.amazon.com/dp/B07MWCDJ9X/',
    	'img': 'https://images-na.ssl-images-amazon.com/images/I/61sHA7o-bxL._SS135_.jpg'
    }, {
    	'id': 'I3C97JA2JR06PN',
    	'title': 'Tenergy Redigrill\xa0Smoke-Less Infrared Grill, Indoor Grill, Heating\xa0Electric Tabletop Grill, Non-Stick Easy to Clean\xa0BBQ Grill, for Party/Home, ETL Certified',
    	'byline': None,
    	'price': '$179.99',
    	'link': 'https://www.amazon.com/dp/B07BZ412HT/',
    	'img': 'https://images-na.ssl-images-amazon.com/images/I/41uGvSPg-ML._SS135_.jpg'
    }, {
    	'id': 'I1C7RJI2H0VWZ7',
    	'title': 'Shelf Liners for Wire Shelf Liner Set of 4 - Graphite (14-Inch-by-36-Inch)',
    	'byline': None,
    	'price': '$29.99',
    	'link': 'https://www.amazon.com/dp/B01N9V4A9A/',
    	'img': 'https://images-na.ssl-images-amazon.com/images/I/71Lg6J7sGHL._SS135_.jpg'
    },
    ...]

Installation
------------

Latest release through PyPI:

.. code-block:: sh

    $ pip install scraper_factory

Development version:

.. code-block:: sh

    $ git clone git@github.com:machinia/scraper-factory.git
    $ cd scraper_factory
    $ pip install -e .


.. |travis| image:: https://img.shields.io/travis/machinia/scraper-factory
    :target: https://travis-ci.org/machinia/scraper-factory
    :alt: Travis Build
.. |coverage| image:: https://coveralls.io/repos/github/machinia/scraper-factory/badge.svg
    :target: https://coveralls.io/github/machinia/scraper-factory
    :alt: Test coverage
.. |pypi| image:: https://badge.fury.io/py/scraper-factory.svg
    :target: https://badge.fury.io/py/scraper-factory
    :alt: PyPI - Latest version
.. |pyversion| image:: https://img.shields.io/pypi/pyversions/scraper_factory
    :target: https://pypi.org/project/scraper-factory/
    :alt: PyPI - Python Version

