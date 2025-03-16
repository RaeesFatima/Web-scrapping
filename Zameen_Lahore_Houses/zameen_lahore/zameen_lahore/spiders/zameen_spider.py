from urllib.parse import urljoin

import scrapy
from ..items import ZameenLahoreItem

class ZameenSpiderSpider(scrapy.Spider):
    name = "zameen"
    start_urls = [
        'https://www.zameen.com/Houses_Property/Lahore-1-1.html'
    ]

    def parse(self, response):
        items=ZameenLahoreItem()
        for house in response.css('li[role=article]'):
            added=house.css('div._11acd4eb span::text').getall()
            home_url = response.urljoin(house.css('article div a::attr(href)').get())
            is_trusted ="yes" if house.css('svg[area-label="Trusted badge"]') else "no"
            deal_type = response.css("div._73e5aa2c div div::text").get()
            is_titanium=response.css("span.b86424a1::text").get()

            items['added']=added
            items['home_url']=home_url
            items['is_trusted'] = is_trusted
            items['deal_type']=deal_type
            items['is_titanium']=is_titanium

            if home_url:
                yield response.follow(items['home_url'],callback=self.parse_house,meta={'items':items})
            else:
                yield items

            # next_page=response.css("a[title='Next']::attr(href)").get()
            # if next_page:
            #     yield response.follow(next_page,callback=self.parse)

    def parse_house(self,response):
        items=response.meta['items']
        items['house_type'] = response.css('span._2fdf7fc5::text').get()
        items['area']=response.css('span._2fdf7fc5 span::text').get()
        items['currency']=response.css('div._2923a568::text').get()
        items['price']= response.css('div._2923a568 span._9e0180f9+ ::text').get()
        items['purpose']=response.css('li:nth-child(6) ._2fdf7fc5::text').get()
        items['location']=response.css('li:nth-child(3) ._2fdf7fc5::text').get()
        items['bath']=response.css("li:nth-child(4) ._2fdf7fc5::text").get()
        items['bedroom']= response.css("li:nth-child(7) ._2fdf7fc5::text").get()
        items['description']= response.css("span._3547dac9::text").getall()
        items['amenities']= response.css("ul._49fc0232 li div::text").getall()

        yield items