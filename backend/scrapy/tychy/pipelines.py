import json
from datetime import date
import time
from .utils import (
    get_newest_stats,
    save_flat_to_db,
    save_statistics_to_db,
    get_newest_flat,
)


class TychyPipeline:
    is_first = True
    save_to_db = False
    save_stats_to_db = False

    total_value = 0
    total_value_known_space = 0

    flat_number = 0

    flat_unknown_price = 0

    total_space = 0
    flat_unknown_space = 0

    estates_list = []

    def process_item(self, item, spider):
        if self.save_to_db:
            save_flat_to_db(item)

        try:
            flat_price = item["price"]
        except:
            flat_price = None

        try:
            flat_space = item["space"]
        except:
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

        self.estates_list.append(dict(item))
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

        line = json.dumps(dict(summary_data), ensure_ascii=False)
        self.file.write(line)

        new_line = "," + "\n"
        self.file.write(new_line)

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
