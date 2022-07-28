import scrapy
from babynames.items import BabynamesItem
from scrapy.loader import ItemLoader


class Babynames_Spider(scrapy.Spider):
    name = 'babynames'
    start_urls = [ "https://babynames.com/"]

    def parse(self, response, **kwargs):
        list_of_alphabets = response.css('ul.browsebyletter a::attr(href)').getall()
        domain_url = 'https://babynames.com'

        for url in list_of_alphabets:
            combine_url = f'{domain_url}{url}'
            yield scrapy.Request(
                url=combine_url,
                callback=self.parse_alphabets
            )

    def parse_alphabets(self, response):
        list_of_names = response.css('ul.searchresults li a::attr(href)').getall()
        domain_url = 'https://babynames.com'
        for names in list_of_names:
            combine_url = f'{domain_url}{names}'
            yield scrapy.Request(
                url=combine_url,
                callback=self.parse_look
            )

    def parse_look(self, response):

        l = ItemLoader(item=BabynamesItem(), response=response)
        l.add_css('Names','h1.baby-name::text')
        l.add_css('gender', 'ul.name-meta li:contains("Gender") a::text')
        l.add_css('origin', 'ul.name-meta li:contains("Origin") a::text')
        l.add_css('meaning', 'li:contains("Meaning")::text')

        yield l.load_item()
