import scrapy
from ..items import FirstscrapyItem
class QuotesSpider(scrapy.Spider):
    name='quotes'       #name of spider
    #below are the urls we want to scrap
    page_number=2
    start_urls=[
        'https://quotes.toscrape.com/page/1/'
        # 'http://quotes.toscrape.com/'
    ]

    def parse(self, response):       #response contains the source code
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

        # next_page=response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page,callback=self.parse)

        #pagination here
        next_page='https://quotes.toscrape.com/page/'+str(QuotesSpider.page_number)+'/'
        if QuotesSpider.page_number<11:
            QuotesSpider.page_number+=1
            yield response.follow(next_page, callback=self.parse)
