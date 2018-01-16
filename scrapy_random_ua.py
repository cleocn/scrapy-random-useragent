#!/usr/bin/python
# -*-coding:utf-8-*-
"""Scrapy Middleware to set a random User-Agent for every Request.

Downloader Middleware which uses a file containing a list of
user-agents and sets a random one for each request.
"""

import random
from fake_useragent import UserAgent
from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

__author__ = "cleocn"
__copyright__ = "Copyright 2017, cleo"
__credits__ = ["cleo"]
__license__ = "MIT"
__version__ = "0.3"
__maintainer__ = "cleo"
__email__ = "cleocn@gmail.com"
__status__ = "Development"


class RandomUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, settings, user_agent='Scrapy'):
        super(RandomUserAgentMiddleware, self).__init__()
        self.ua = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls(crawler.settings)
        crawler.signals.connect(obj.spider_opened,
                                signal=signals.spider_opened)
        return obj

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random )
