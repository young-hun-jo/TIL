# -*- coding: utf-8 -*-
import scrapy
from crawl_11st.items import Crawl11StItem

class Crawl11stBestSpider(scrapy.Spider):
    name = 'crawl_11st_best'
    
    def start_requests(self):
        yield scrapy.Request(url='http://www.11st.co.kr/html/dealBest1.html', callback=self.parse_all_category)

    def parse_all_category(self, response):
    	print("cateogry_all")
    	category_names = response.css("div.ranking_cate.shockdeal ul li a::text").getall()
    	category_links = response.css("div.ranking_cate.shockdeal ul li a::attr(href)").getall()
    	# 모든 카테고리에 request 요청
    	for index, category_link in enumerate(category_links):
    		yield scrapy.Request(url=category_link, callback=self.parse_contents,
    			meta={'category_name':category_names[index]})

    def parse_contents(self, response):
    	print("category name: ", response.meta['category_name'])
    	best_lists = response.css("div.thumbnail_list ul li")
    	for index, best_list in enumerate(best_lists):
    		doc = Crawl11StItem()
    		title = best_list.css("div.product_conts div.pup_title a::text").get()
    		ori_price = best_list.css("div.product_conts div.pub_priceW s::text").get()
    		dis_price = best_list.css("div.product_conts div.pub_priceW strong.pub_salep::text").get()
    		dis_rate = best_list.css("div.product_conts div.pub_priceW div.sale_per span.sale_arrow::text").get()
    		if dis_price is None:
    			dis_price = ori_price
    		if dis_rate is None:
    			dis_rate = "0%"
    		ori_price = int(ori_price.replace(",","").replace("원","").replace("~",""))
    		dis_price = int(dis_price.replace(",","").replace("원","").replace("~",""))
    		dis_rate = int(dis_rate.replace("%",""))
    		#print(title, ori_price, dis_price, dis_rate)
    		doc['product_title'] = title
    		doc['category_name'] = response.meta['category_name']
    		doc['original_price'] = ori_price
    		doc['discount_price'] = dis_price
    		doc['discount_rate'] = dis_rate

    		yield doc
    		



