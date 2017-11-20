# -*- coding: utf-8 -*-
import scrapy
from test_scrapy import items


class GoogleSpider(scrapy.Spider):
    name = 'google'
    allowed_domains = ['google.com','google.com.ua']
    start_urls = ['https://google.com/']

    def parse_results(self, response):
        links = response.xpath('//h3[contains(@class,"r")]/a')
        for link in links:
            name = link.xpath('@href').extract()
            link1 = ''.join(link.xpath('.//text()').extract())
            item = items.SearchItem()
            item['name'] = name
            item['link'] = link1
            yield item

    def parse(self, response):
        search_url = 'https://www.google.com.ua/search?q={}'.format('python')
        yield scrapy.Request(url=search_url, callback=self.parse_results)






