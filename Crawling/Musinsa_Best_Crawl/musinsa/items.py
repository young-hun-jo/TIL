# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusinsaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Brand = scrapy.Field()
    Product = scrapy.Field()
    Price = scrapy.Field()
    Like = scrapy.Field()

