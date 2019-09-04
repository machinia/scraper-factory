LOG_LEVEL = 'ERROR'
FEED_FORMAT = 'json'

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}

# RandomUserAgentMiddleware settings
RANDOM_UA_TYPE = 'random'
