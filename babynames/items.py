import scrapy
from scrapy.loader import ItemLoader


class BabynamesItem(scrapy.Item):

     Names = scrapy.Field()
     gender = scrapy.Field()
     origin = scrapy.Field()
     meaning = scrapy.Field()
