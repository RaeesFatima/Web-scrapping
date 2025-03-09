# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from urllib.parse import quote

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FirstscrapyPipeline:
    def process_item(self, item, spider):
        item['quote']=item['quote'][0].strip() if item['quote'] else ''
        item['author']=item['author'][0].strip() if item['author'] else ''
        item['tag']=[t.strip() for t in item['tag']] if item['tag'] else ''
        return item
