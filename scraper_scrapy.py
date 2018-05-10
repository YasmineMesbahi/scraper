""" Creating a scraper using scrapy """
# -*- coding: utf8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    # url to scrape
    start_urls = ['https://fr.wikipedia.org/wiki/Liste_de_langages_de_programmation']

    def parse(self, response):
        # css selector
        for title in response.css('div.mw-parser-output li'):
            yield {'language': title.css('a ::text').extract_first()}
