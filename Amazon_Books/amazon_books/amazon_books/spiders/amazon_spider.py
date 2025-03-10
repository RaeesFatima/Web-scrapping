import scrapy
from ..items import  AmazonBooksItem
class AmazonSpiderSpider(scrapy.Spider):

    name = "amazon"
    start_urls = [
        'https://www.amazon.com/s?k=books+for+kids&i=stripbooks-intl-ship&rh=n%3A283155%2Cp_n_feature_three_browse-bin%3A1250579011&dc&ds=v1%3AX4HBMRLtR%2BZOqapgqyrltOYsGSBsyTH6Ndj3XVhi5iM&crid=3VW3QH0A7061F&qid=1741602011&rnid=1250577011&sprefix=book%2Cstripbooks-intl-ship%2C1111&ref=sr_nr_p_n_feature_three_browse-bin_1'

    ]

    def parse(self, response):
        items=AmazonBooksItem()
        for books in response.css('div.puisg-row'):
            title = books.css('a.a-link-normal.s-line-clamp-2.s-link-style.a-text-normal h2 span::text').get(default='Unknown Title')
            authors=books.css('div.a-row.a-size-base.a-color-secondary span.a-size-base+ a::text').getall()
            author = ', '.join(authors) if authors else 'Unknown Author'
            price=books.css('span.a-price span.a-offscreen::text').get(default='price not found')
            img_link=books.css('.s-image::attr(src)').get(default='no img found')
            items['title']=title
            items['author']=author
            items['price']=price
            items['img_link']=img_link
            print('here are the titles', response.text)
            if title != "Unknown Title" or author != "Unknown Author":
                yield items

        now=1
        next_page = response.css('a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-button-accessibility.s-pagination-separator::attr(href)').get()
        self.logger.info(f'Next page found: {now}')
        if next_page:
            now+=1
            yield response.follow(next_page, callback=self.parse)
