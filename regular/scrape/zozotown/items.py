# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class BrandItem(scrapy.Item):
    brand_id = scrapy.Field(output_processor=TakeFirst())
    brand_name = scrapy.Field(output_processor=TakeFirst())
    brand_name_kana = scrapy.Field(output_processor=TakeFirst())
    brand_url = scrapy.Field(output_processor=TakeFirst())
    created_at = scrapy.Field(output_processor=TakeFirst())
