# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GmarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    main_category_name = scrapy.Field()
    sub_category_name = scrapy.Field()
    title = scrapy.Field()
    ori_price = scrapy.Field()
    dis_price = scrapy.Field()
    dis_rate = scrapy.Field()
    
    

