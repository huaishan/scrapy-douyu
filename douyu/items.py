# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    room_name = scrapy.Field()
    tag = scrapy.Field()
    people_count = scrapy.Field()
    anchor = scrapy.Field()
    real_people_count = scrapy.Field()
