# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JobcrawlerPipeline(object):
    def process_item(self, item, spider):
        print "item is pipeline is", item
        item['no_of_vacancy'] = self.cleanup_address(item['no_of_vacancy'])
        item.save()
        return item

    def cleanup_address(self, no_of_vacancy):
        print 'vacancy is', no_of_vacancy
        return no_of_vacancy
