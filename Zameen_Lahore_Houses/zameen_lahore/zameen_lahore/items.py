# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZameenLahoreItem(scrapy.Item):
    # define the fields for your item here like:
    added = scrapy.Field()
    home_url = scrapy.Field()
    is_trusted=scrapy.Field()
    deal_type=scrapy.Field()
    house_type=scrapy.Field()
    area = scrapy.Field()
    currency=scrapy.Field()
    price=scrapy.Field()
    purpose=scrapy.Field()
    location=scrapy.Field()
    bath=scrapy.Field()
    bedroom=scrapy.Field()
    description=scrapy.Field()
    amenities=scrapy.Field()
    is_titanium=scrapy.Field()