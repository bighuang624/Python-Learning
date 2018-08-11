# !/usr/bin/env python3
# -*- coding: utf-8 -*-


from scrapy import Request
from scrapy.spiders import Spider
from scrapyspider.items import DoubanMovieItem

class DoubanMovieTop250Spider(Spider):
    # name : 用于区别 Spider，必须唯一
    name = 'douban_movie_top250'
    # start_urls : 包含了Spider在启动时进行爬取的url列表。 
    # 因此，第一个被获取到的页面将是其中之一。 
    # 后续的URL则从初始的URL获取到的数据中提取。
    # start_urls = ['https://movie.douban.com/top250']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    # 
    def parse(self, response):
        item = DoubanMovieItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath(
                './/div[@class="pic"]/em/text()').extract()[0]
            item['movie_name'] = movie.xpath(
                './/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = movie.xpath(
                './/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num'] = movie.xpath(
                './/div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)
