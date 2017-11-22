# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from util.proxyPoolUtil import ProxyPoolUtil

import random

class RandomUserAgentMiddleware(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    # 从crawler构造，USER_AGENTS定义在crawler的配置的设置中
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    # 从settings构造，USER_AGENTS定义在settings.py中
    @classmethod
    def from_settings(cls, settings):
        return cls(settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        #设置代理IP
        romProxy=ProxyPoolUtil.get_proxy()
        request.meta['proxy'] = "http://{}".format(romProxy.decode())
        # 设置随机的User-Agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            romProxy = ProxyPoolUtil.get_proxy()
            request.meta['proxy'] = "http://{}".format(romProxy.decode())
            return request
        return response

