# -*- coding: utf-8 -*-
import scrapy
from test_scrapy import items


class GoogleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['http://www.lordandtaylor.com']
    start_urls = ['http://www.lordandtaylor.com/Shoes/shop/_/N-4ztf0d/Ne-6ja3o7']

    def parse_category(self, response):
        categories = response.xpath('//li[contains(@class, "left-nav-list-show")]/ul/li/a[!contains(@class, "selected")]')
        for category in categories:
            link = category.xpath('@href').extract_first()
            name = category.xpath('text()').extract_first()
            item = items.SearchItem()
            item['name'] = name
            item['link'] = link
            yield item

    def parse(self, response):
        categories = response.xpath('//li[contains(@class, "left-nav-list-hide")]/a')
        for category in categories:
            link = category.xpath('@href').extract_first()
            name = category.xpath('text()').extract_first()
            yield scrapy.Request(url=link, meta={'category': [name]}, callback=self.parse_category)