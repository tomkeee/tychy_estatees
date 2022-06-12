import time
import scrapy
from scrapy.loader import ItemLoader
import os

os.environ["PYTHONHOME"] = "/code"

from tychy.items import EstatesItem

from tychy.filters.top_information import (
    get_price,
    get_space,
    get_flat_status,
    get_flat_floor,
    get_form_of_ownership,
    get_flat_heating,
    has_flat_car_park,
    get_flat_additionals,
    get_flat_market,
    get_advertiser_type,
    get_type_of_building,
    has_flat_elevator,
    get_flat_window,
    get_flat_media,
    get_build_year,
    get_building_material,
)


class OtodomSpider(scrapy.Spider):
    name = "otodom"
    allowed_domains = [
        "www.otodom.pl",
    ]

    start_urls = ["https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/tychy"]

    page_nr_int = 1

    page_nr_str = str(page_nr_int)

    url_pagination = start_urls[0] + "?page=" + page_nr_str

    def parse(self, response):
        resp = response.xpath("//div[@data-cy='no-search-results']")
        if len(resp) == 0:
            self.page_nr_int += 1
            self.page_nr_str = str(self.page_nr_int)
            self.url_pagination = self.start_urls[0] + "?page=" + self.page_nr_str
            yield scrapy.Request(url=self.url_pagination, callback=self.parse)
        else:
            pass

        articles = response.xpath("//a[contains(@data-cy, 'listing-item-link')]")

        for article in articles:
            link = "https://www.otodom.pl/" + article.xpath(".//@href").get()
            title = article.xpath(".//article/div/h3/text()").get()
            localization = article.xpath(".//article/p/span/text()").get()
            price = article.xpath(".//article/div/span/text()").get()

            spans = article.xpath(".//article/div/span/text()").getall()
            price = spans[0]

            flat_price = get_price(price)

            yield response.follow(
                url=link,
                callback=self.parse_offer,
                cb_kwargs={
                    "article": article,
                    "link": link,
                    "title": title,
                    "localization": localization,
                    "price": flat_price,
                },
            )

    def parse_offer(self, response, article, link, title, localization, price):
        rent_response = response.xpath(
            "//div[@aria-label='Czynsz']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_rent = get_space(rent_response)

        space_response = response.xpath(
            "//div[@aria-label='Powierzchnia']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()

        flat_space = get_space(space_response)

        room_number_response = response.xpath(
            "//div[@aria-label='Liczba pokoi']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_room_number = get_price(room_number_response)

        flat_status_response = response.xpath(
            "//div[@aria-label='Stan wykończenia']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_status = get_flat_status(flat_status_response)

        flat_floor_response = response.xpath(
            "//div[@aria-label='Piętro']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_floor = get_flat_floor(flat_floor_response)

        flat_form_of_ownership_response = response.xpath(
            "//div[@aria-label='Forma własności']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_form_of_ownership = get_form_of_ownership(flat_form_of_ownership_response)

        flat_heating_response = response.xpath(
            "//div[@aria-label='Ogrzewanie']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_heating = get_flat_heating(flat_heating_response)

        flat_car_park_response = response.xpath(
            "//div[@aria-label='Miejsce parkingowe']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_car_park = has_flat_car_park(flat_car_park_response)

        flat_additionals_details_field_response = response.xpath(
            "//div[@aria-label='Balkon / ogród / taras']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_additionals_information_response = response.xpath(
            "//div[@aria-label='Informacje dodatkowe']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()

        flat_additionals = get_flat_additionals(
            flat_additionals_details_field_response,
            flat_additionals_information_response,
        )

        flat_market_reposnse = response.xpath(
            "//div[@aria-label='Rynek']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_market = get_flat_market(flat_market_reposnse)

        advertiser_type_response = response.xpath(
            "//div[@aria-label='Typ ogłoszeniodawcy']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        advertiser_type = get_advertiser_type(advertiser_type_response)

        type_of_building_response = response.xpath(
            "//div[@aria-label='Rodzaj zabudowy']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        type_of_building = get_type_of_building(type_of_building_response)

        flat_elevator_response = response.xpath(
            "//div[@aria-label='Winda']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_elevator = has_flat_elevator(flat_elevator_response)

        flat_window_response = response.xpath(
            "//div[@aria-label='Okna']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_window = get_flat_window(flat_window_response)

        flat_media_response = response.xpath(
            "//div[@aria-label='Media']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        flat_media = get_flat_media(flat_media_response)

        build_year_response = response.xpath(
            "//div[@aria-label='Rok budowy']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        build_year = get_build_year(build_year_response)

        building_material_response = response.xpath(
            "//div[@aria-label='Materiał budynku']//div[@class='css-1wi2w6s estckra5']/text()"
        ).get()
        building_material = get_building_material(building_material_response)

        loader = ItemLoader(item=EstatesItem(), selector=article, response=response)

        loader.add_value("link", link)
        loader.add_value("title", title)
        loader.add_value("localization", localization)
        loader.add_value("price", price)
        loader.add_value("rent", flat_rent)
        loader.add_value("rooms", flat_room_number)
        loader.add_value("space", flat_space)
        loader.add_value("status", flat_status)
        loader.add_value("ownership", flat_form_of_ownership)
        loader.add_value("heating", flat_heating)
        loader.add_value("car_park", flat_car_park)
        loader.add_value("market", flat_market)
        loader.add_value("advertiser_type", advertiser_type)
        loader.add_value("type_of_building", type_of_building)
        loader.add_value("elevator", flat_elevator)
        loader.add_value("flat_window", flat_window)
        loader.add_value("build_year", build_year)
        loader.add_value("building_material", building_material)

        loader.add_value("flat_media", flat_media)

        loader.add_value("floor", flat_floor)
        loader.add_value("additionals", flat_additionals)

        yield loader.load_item()
