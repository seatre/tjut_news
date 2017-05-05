# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TjutNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    news_url=scrapy.Field()
    news_title=scrapy.Field()
    news_datetime=scrapy.Field()
