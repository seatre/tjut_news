# encoding: utf-8
# Created by seatre on 2017/5/5

import scrapy
import scrapy.shell
from bs4 import BeautifulSoup
import lxml
import time
from tjut_news.items import TjutNewsItem
import datetime


class SpiderSpider(scrapy.Spider):
    name = "tjut_news"
    # allowed_domains = ["jd.com"]
    # start_urls = ['http://jd.com/']
    start_url = 'http://news.tjut.edu.cn/yw.htm'

    def start_requests(self):
        yield scrapy.Request(self.start_url,
                             callback=self.parse_url)  # 这里使用meta想回调函数传入数据，回调函数使用response.meta['search-page']接受数据

    def parse_url(self, response):
        global datetime
        if response.status == 200:
            try:
                all_news = response.xpath("//tr[contains(@id,'line52564')]")

                for news in all_news:
                    # scrapy.shell.inspect_response(response,self)
                    items = TjutNewsItem()
                    news_title = news.xpath(".//a[@class='c52564']/text()").extract()

                    news_url = news.xpath(".//a[@class='c52564']/@href").extract()
                    news_datetime = news.xpath(".//span[@class='timestyle52564']/text()").extract()
                    # product_id=goods.xpath("@data-sku").extract()

                    if news_title:
                        temp = news_title[0]
                        items['news_title'] = "".join(temp.split())


                    if news_url:
                        temp = "http://news.tjut.edu.cn/" + news_url[0]
                        items['news_url'] = "".join(temp.split())

                    if news_datetime:
                        temp = news_datetime[0]
                        temp1 = "".join(temp.split())
                        items['news_datetime'] = temp1
                        #dt = datetime.datetime.strptime(temp1, "%Y/%m/%d")

                    yield
                    # if product_id:
                    #     print "************************************csdjkvjfskvnk***********************"
                    #     print self.comments_url.format(str(product_id[0]),str(self.count))
                    #     yield scrapy.Request(url=self.comments_url.format(str(product_id[0]),str(self.count)),callback=self.comments)
                    # yield scrapy.Request写在这里就是每解析一个键裤子就会调用回调函数一次
                    yield items
            except Exception:
                print "********************************************ERROR**********************************************************************"

