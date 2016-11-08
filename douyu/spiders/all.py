# -*- coding: utf-8 -*-
import scrapy
from scrapy import log
from scrapy.http.request import Request

from douyu.items import DouyuItem


class AllSpider(scrapy.Spider):
    name = "all"
    allowed_domains = ["douyu.com"]
    start_urls = ['https://www.douyu.com/directory/all']

    domain = 'https://www.douyu.com'
    url_temp = 'https://www.douyu.com/directory/all?page={page}&isAjax=1'

    page_count = None
    page_count_rule = "//a[@data-href='/directory/all']/@data-pagecount"

    def check_page_count(self, response):
        if not self.page_count:
            self.page_count = int(response.xpath(self.page_count_rule).extract()[0])

    def parse(self, response):
        log.msg('Parse '+response.url)

        self.check_page_count(response)

        for i in range(1, self.page_count+1):
            yield Request(url=self.url_temp.format(page=i), callback=self.parse_item)

    @staticmethod
    def get_list(l):
        return l[0] if l else ''

    @staticmethod
    def real_people_count(people_count):
        if u'万' in people_count:
            people_count = people_count.replace(u'万', '')
            return int(float(people_count) * 10000)
        return int(people_count)

    def parse_item(self, response):
        for sel in response.xpath("//li"):
            item = DouyuItem()
            item['url'] = self.domain + self.get_list(sel.xpath("a/@href").extract())
            item['room_name'] = self.get_list(sel.xpath("a/@title").extract())
            item['tag'] = self.get_list(sel.xpath("a/div/div/span/text()").extract())
            item['people_count'] = self.get_list(sel.xpath("a/div/p/span[@class='dy-num fr']/text()").extract())
            item['anchor'] = self.get_list(sel.xpath("a/div/p/span[@class='dy-name ellipsis fl']/text()").extract())
            item['real_people_count'] = self.real_people_count(item['people_count'])
            yield item
