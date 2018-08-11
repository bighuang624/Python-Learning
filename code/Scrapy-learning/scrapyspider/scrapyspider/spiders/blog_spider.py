# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 启动 : scrapy crawl blogSpider

from scrapy.spiders import Spider

class BlogSpider(Spider):
    # name : 用于区别 Spider，必须唯一
    name = 'blogSpider'
    # start_urls : 包含了Spider在启动时进行爬取的url列表。 
    # 因此，第一个被获取到的页面将是其中之一。 
    # 后续的URL则从初始的URL获取到的数据中提取。
    start_urls = ['http://woodenrobot.me']

    # 
    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())

