import scrapy
from ..items import FirstscrapyItem
class QuotesSpider(scrapy.Spider):
    name='quotes'       #name of spider
    #below are the urls we want to scrap
    start_urls=[
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):       #response contains the source code which here is title text
        all_div_quotes=response.css('div.quote')
        items=FirstscrapyItem()
        for quotes in all_div_quotes:
            quote=quotes.css('span.text::text').extract()
            author=quotes.css('.author::text').extract()
            tag=quotes.css('.tag::text').extract()

            items['quote']=quote
            items['author']=author
            items['tag']=tag

            yield items

        next_page=response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)