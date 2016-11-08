# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from datetime import datetime

from scrapy import log
from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.Connection(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION'] +
                             datetime.now().strftime('%Y%m%d%H%M%S')]

    def process_item(self, item, spider):
        if item:
            self.collection.insert(dict(item))
            log.msg('Added to MongoDB database success!',
                    level=log.DEBUG, spider=spider)
        else:
            raise DropItem('Missing {0}'.format(item))

        return item
