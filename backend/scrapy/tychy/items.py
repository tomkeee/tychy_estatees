import scrapy
from itemloaders.processors import TakeFirst


class EstatesItem(scrapy.Item):
    link = scrapy.Field(output_processor=TakeFirst())
    title = scrapy.Field(output_processor=TakeFirst())
    localization = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    rent = scrapy.Field(output_processor=TakeFirst())

    rooms = scrapy.Field(output_processor=TakeFirst())
    space = scrapy.Field(output_processor=TakeFirst())
    status = scrapy.Field(output_processor=TakeFirst())
    ownership = scrapy.Field(output_processor=TakeFirst())
    heating = scrapy.Field(output_processor=TakeFirst())

    car_park = scrapy.Field(output_processor=TakeFirst())
    market = scrapy.Field(output_processor=TakeFirst())
    advertiser_type = scrapy.Field(output_processor=TakeFirst())
    type_of_building = scrapy.Field(output_processor=TakeFirst())
    elevator = scrapy.Field(output_processor=TakeFirst())

    flat_window = scrapy.Field(output_processor=TakeFirst())
    build_year = scrapy.Field(output_processor=TakeFirst())
    building_material = scrapy.Field(output_processor=TakeFirst())

    additionals = scrapy.Field()
    flat_media = scrapy.Field()
    floor = scrapy.Field(output_processor=TakeFirst())
