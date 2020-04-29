# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawl11StItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category_name = scrapy.Field()
    product_title = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    discount_rate = scrapy.Field()
