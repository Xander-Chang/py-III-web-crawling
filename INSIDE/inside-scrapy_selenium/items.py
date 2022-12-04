# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProject8Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_title = scrapy.Field()
    post_date = scrapy.Field()
    post_author = scrapy.Field()

