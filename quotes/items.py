from scrapy import Field, Item
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader

def remove_quotes(text):
    return text.strip().strip(u"\u201c").strip(u"\u201d")

def remove_whitespace(text):
    t = text.strip()
    if t.endswith(','):
        t = t[:-1]
    return t

class QuotesItem(Item):
    quote = Field(
        input_processor=MapCompose(remove_quotes),
        output_processor=TakeFirst()
    )
    tags = Field()
    author = Field(
        input_processor=MapCompose(remove_whitespace),
        output_processor=TakeFirst()
    )
    author_img = Field(
        output_processor=TakeFirst()
    )
