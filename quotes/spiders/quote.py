import scrapy
from quotes.items import QuotesItem
from scrapy.loader import ItemLoader


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['goodreads.com']
    start_urls = [
        # 'https://www.goodreads.com/quotes',
        # 'https://www.goodreads.com/quotes/tag/life',
        'https://www.goodreads.com/quotes/tag/time',
        'https://www.goodreads.com/quotes/tag/death'
    ]

    def parse(self, response):
        self.logger.info("Started!!!!")
        quotes = response.css("div.quote")
        for quote in quotes:
            loader = ItemLoader(item=QuotesItem(), selector=quote)
            loader.add_css("quote", "div.quoteText::text")
            loader.add_css("author", "span.authorOrTitle::text")
            loader.add_css("author_img", "a.leftAlignedImage > img::attr(src)")
            loader.add_css("tags", "div.quoteFooter > div.greyText > a::text")
            quote_item = loader.load_item()
            yield quote_item

        next_page = response.css('a.next_page::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)