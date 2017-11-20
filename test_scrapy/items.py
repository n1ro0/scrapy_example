# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SearchItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()


class ProductItem(scrapy.Item):
    site_product_id = scrapy.Field()
    name = scrapy.Field()
    brand = scrapy.Field()
    categories = scrapy.Field()
    description = scrapy.Field()
    material = scrapy.Field()
    made_in = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()
    site = scrapy.Field()

