# -*- coding: utf-8 -*-
import scrapy
from gmarket.items import GmarketItem

class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'
    	#이름 fix
    def start_requests(self):
    	yield scrapy.Request(url="http://corners.gmarket.co.kr/Bestsellers", callback=self.parse_all)


    def parse_all(self, response):
        print("parse_all")
        category_names = response.css("div.gbest-cate > ul.by-group > li > a::text").getall()
        category_links = response.css("div.gbest-cate > ul.by-group > li > a::attr(href)").getall()
        # 1st category
        for index, category_link in enumerate(category_links):
        	yield scrapy.Request(url="http://corners.gmarket.co.kr"+category_link, callback=self.parse_contents,
        		meta={'main_category_name':category_names[index], 'sub_category_name':'ALL'})
        		# meta : 다음 함수(여기서는 parse_contents)로 이름 전달할 수있음 출력하도록 하기 위해
        # 2nd category
        for index, category_link in enumerate(category_links):
        	yield scrapy.Request(url="http://corners.gmarket.co.kr"+category_link, callback=self.parse_subcategory,
        		meta={'sub_category_name':sub_category_name[index]})

    def parse_subcategory(self, resonse):
    	print("parse_subcategory", response.meta['sub_category_name'])
    	sub_category_name = response.css("div.navi.group > ul > li > a::text").getall()
    	subcategory_links = response.css("div.navi.group > ul > li > a::attr(href)").getall()
    	for index, subcategory_link in enumerate(subcategory_links):
        	yield scrapy.Request(url="http://corners.gmarket.co.kr"+subcategory_link, callback=self.parse_contents,
        		meta={'main_category_name':category_names[index], 'sub_category_name':sub_category_name[index]})

    def parse_contents(self, response):
    	print("parse_maincategory", response.meta['main_category_name'])
    	best_lists = response.css("div.best-list")
    	for index, best_list in enumerate(best_lists[1].css("li")):
    		doc = GmarketItem()
    		title = best_list.css("a.itemname ::text").get()
    		ori_price = best_list.css("div.o-price::text").get()
    		dis_price = best_list.css("div.s-price strong span span::text").get()
    		dis_rate = best_list.css("div.s-price span em::text").get()
    		if ori_price is None:
    			ori_price = dis_price
    		ori_price = ori_price.replace(",","").replace("원","")
    		dis_price = dis_price.replace(",","").replace("원","")
    		if dis_rate is None:
    			dis_rate = "0"
    		else:
    			dis_rate = dis_rate.replace("%","")

    		#print(title, ori_price, dis_price, dis_rate)
    		doc['main_category_name'] = response.meta['main_category_name']
    		doc['sub_category_name'] = response.meta['sub_category_name']
    		doc['title'] = title
    		doc['ori_price'] = ori_price
    		doc['dis_price'] = dis_price
    		doc['dis_rate'] = dis_rate

    		yield doc
    		 		
    		

    
