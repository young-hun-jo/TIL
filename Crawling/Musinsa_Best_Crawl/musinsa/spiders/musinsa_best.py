# -*- coding: utf-8 -*-
import scrapy
from musinsa.items import MusinsaItem

class MusinsaBestSpider(scrapy.Spider):
    name = 'musinsa_best'
    allowed_domains = ['store.musinsa.com/app/contents/bestranking']
    start_urls = ['http://store.musinsa.com/app/contents/bestranking/']

    def parse(self, response):
    	Brands = response.css("div.article_info p.item_title a::text").getall()
    	Products = response.css("div.article_info p.list_info a ::attr('title')").getall()
    	Origin_prices = response.css("div.article_info p.price del ::text").getall()
    	Likes_num = response.css("div.article_info p.txt_cnt_like ::text").getall()[1::2]
    	for i in range(len(Products)):
    		item = MusinsaItem()
    		item['Brand'] = Brands[i]
    		item['Product'] = Products[i]
    		item['Price'] = int(Origin_prices[i].replace("원","").replace(",",""))
    		item['Like'] = Likes_num[i].strip("\n").strip("\t").strip('\t').strip('\t').strip('\t').strip('\n')
    		yield item

