import json
from datetime import date
import time
from .utils import (
    get_newest_stats,
    save_flat_to_db,
    save_statistics_to_db,
    get_newest_flat,
    save_districts_to_db,
    save_streets_to_db,
    add_dict_to_json,
    get_newest_location_streets,
    get_newest_location_districts,
)

from tychy.filters.top_information import (
    get_district,
    DISTRICTS,
)


class TychyPipeline:
    is_first = True
    save_to_db = False
    save_stats_to_db = False
    save_streets_to_db = False
    save_districts_to_db = False

    total_value = 0
    total_value_known_space = 0

    flat_number = 0

    flat_unknown_price = 0

    total_space = 0
    flat_unknown_space = 0

    estates_list = []

    streets = {}
    districts = {}

    def process_item(self, item, spider):
        try:
            flat_price = item["price"]
        except:
            item["price"] = None
            flat_price = None

        try:
            flat_space = item["space"]
        except:
            item["space"] = None
            flat_space = None

        if flat_price and flat_space:
            self.flat_number += 1
            self.total_value += flat_price

            self.total_value_known_space += flat_price
            self.total_space += flat_space

        elif flat_price and not flat_space:
            self.flat_number += 1
            self.total_value += flat_price
            self.flat_unknown_space += 1

        elif flat_space and not flat_price:
            self.flat_number += 1
            self.flat_unknown_price += 1

        else:
            self.flat_unknown_price += 1
            self.flat_unknown_space += 1
            self.flat_number += 1

        item_as_dict = dict(item)
        item_as_dict["district"] = None
        item_as_dict["street"] = None

        localization_details = get_district(item["localization"])

        if localization_details in DISTRICTS:
            item_as_dict["district"] = localization_details
            if localization_details in self.districts.keys():
                self.districts[localization_details]["flat_number"] += 1
                if item["price"] is not None:
                    self.districts[localization_details]["flats_value"] += item["price"]
                    self.districts[localization_details]["flats_number_value"] += 1
                if (item["price"] is not None) and (item["space"] is not None):
                    self.districts[localization_details]["flats_space"] += item["space"]
                    self.districts[localization_details]["flats_value_space"] += item[
                        "price"
                    ]
                    self.districts[localization_details]["flats_number_space"] += 1

            else:
                self.districts[localization_details] = {
                    "flat_number": 1,
                    "flats_number_value": 0,
                }
                if item["price"] is not None:
                    self.districts[localization_details]["flats_value"] = item["price"]
                    self.districts[localization_details]["flats_number_value"] = 1
                else:
                    self.districts[localization_details]["flats_value"] = 0
                    self.districts[localization_details]["flats_number_value"] = 0

                if (item["price"] is not None) and (item["space"] is not None):
                    self.districts[localization_details]["flats_space"] = item["space"]
                    self.districts[localization_details]["flats_value_space"] = item[
                        "price"
                    ]
                    self.districts[localization_details]["flats_number_space"] = 1
                else:
                    self.districts[localization_details]["flats_space"] = 0
                    self.districts[localization_details]["flats_value_space"] = 0
                    self.districts[localization_details]["flats_number_space"] = 0

        elif localization_details:
            item_as_dict["street"] = localization_details
            if localization_details in self.streets.keys():
                self.streets[localization_details]["flat_number"] += 1
                if item["price"] is not None:
                    self.streets[localization_details]["flats_value"] += item["price"]
                    self.streets[localization_details]["flats_number_value"] += 1
                if (item["price"] is not None) and (item["space"] is not None):
                    self.streets[localization_details]["flats_space"] += item["space"]
                    self.streets[localization_details]["flats_value_space"] += item[
                        "price"
                    ]
                    self.streets[localization_details]["flats_number_space"] += 1

            else:
                self.streets[localization_details] = {
                    "flat_number": 1,
                    "flats_number_value": 0,
                }
                if item["price"] is not None:
                    self.streets[localization_details]["flats_value"] = item["price"]
                    self.streets[localization_details]["flats_number_value"] = 1
                else:
                    self.streets[localization_details]["flats_value"] = 0
                    self.streets[localization_details]["flats_number_value"] = 0
                if (item["price"] is not None) and (item["space"] is not None):
                    self.streets[localization_details]["flats_space"] = item["space"]
                    self.streets[localization_details]["flats_value_space"] = item[
                        "price"
                    ]
                    self.streets[localization_details]["flats_number_space"] = 1
                else:
                    self.streets[localization_details]["flats_space"] = 0
                    self.streets[localization_details]["flats_value_space"] = 0
                    self.streets[localization_details]["flats_number_space"] = 0

        if self.save_to_db:
            save_flat_to_db(item, item_as_dict["district"], item_as_dict["street"])
        self.estates_list.append(item_as_dict)
        return item

    def open_spider(self, spider):
        flat = get_newest_flat()
        if flat is None or flat.date != date.today():
            self.save_stats_to_db = True
        else:
            self.save_stats_to_db = False

        stat = get_newest_stats()
        if stat is None or stat.date != date.today():
            self.save_to_db = True
        else:
            self.save_to_db = False

        street = get_newest_location_streets()
        if street is None or street.date != date.today():
            self.save_streets_to_db = True
        else:
            self.save_streets_to_db = False

        district = get_newest_location_districts()
        if district is None or district.date != date.today():
            self.save_districts_to_db = True
        else:
            self.save_districts_to_db = False

    def close_spider(self, spider):
        today = date.today()

        self.file = open(
            f"/code/data/otodom_{today.strftime('%d_%m_%Y')}.json",
            "w",
            encoding="utf8",
        )
        self.file.write("[" + "\n")

        summary_data = {
            "flat_number": self.flat_number,
            "flat_average_price": self.total_value
            / (self.flat_number - self.flat_unknown_price),
            "flat_m2_average_price": self.total_value_known_space / self.total_space,
        }

        add_dict_to_json(summary_data, self.file)

        for i in self.streets:
            self.streets[i]["flat_average_price"] = (
                self.streets[i]["flats_value"] / self.streets[i]["flats_number_value"]
            )
            self.streets[i]["flat_m2_average_price"] = (
                self.streets[i]["flats_value_space"] / self.streets[i]["flats_space"]
            )

            if self.save_streets_to_db:
                save_streets_to_db(
                    location=i,
                    flat_number=self.streets[i]["flat_number"],
                    flat_average_price=self.streets[i]["flat_average_price"],
                    flat_average_rent=None,
                    flat_m2_average_price=self.streets[i]["flat_m2_average_price"],
                )

        add_dict_to_json(self.streets, self.file)

        for i in self.districts:
            self.districts[i]["flat_average_price"] = (
                self.districts[i]["flats_value"]
                / self.districts[i]["flats_number_value"]
            )
            self.districts[i]["flat_m2_average_price"] = (
                self.districts[i]["flats_value_space"]
                / self.districts[i]["flats_space"]
            )

            if self.save_districts_to_db:
                save_districts_to_db(
                    location=i,
                    flat_number=self.districts[i]["flat_number"],
                    flat_average_price=self.districts[i]["flat_average_price"],
                    flat_average_rent=None,
                    flat_m2_average_price=self.districts[i]["flat_m2_average_price"],
                )

        add_dict_to_json(self.districts, self.file)

        for i in self.estates_list:
            if self.is_first:
                self.is_first = False
                line = json.dumps(dict(i), ensure_ascii=False)
            else:
                line = "," + "\n" + json.dumps(dict(i), ensure_ascii=False)

            self.file.write(line)

        line = "\n" + "]"
        self.file.write(line)
        self.file.close()

        if self.save_stats_to_db:
            save_statistics_to_db(summary_data)
