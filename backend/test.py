import json
from scrapy.tychy.utils import save_flat_to_db,save_statistics_to_db,save_streets_to_db,save_districts_to_db
from datetime import date

with open("/code/data/otodom_02_07_2022.json", "r") as read_file:
            data = json.load(read_file)

            new_value = "02_07_2022".split("_")
            given_date = []
            print(new_value)
            given_date.append(int(new_value[0]))
            given_date.append(int(new_value[1]))
            given_date.append(int(new_value[2]))

            for i in data:
                if "bielska" in list(i.keys()):
                    for street in i:
                        print()
                        print()
                        print()
                        print()
                        print(list(i.keys()))
                        print()
                        print(i[street])
                        print()
                        print()
                        print()
                        save_streets_to_db(
                        location=street,
                        flat_number=i[street]["flat_number"],
                        flat_average_price=i[street]["flat_average_price"],
                        flat_average_rent=None,
                        flat_m2_average_price=i[street]["flat_m2_average_price"],
                        date=date(given_date[2],given_date[1],given_date[0])
                    )
                if "żwaków" in list(i.keys()):
                    for district in i:
                        print()
                        print()
                        print()

                        print(district)
                        print()
                        print()
                        print()
                        print()
                        save_districts_to_db(
                        location=district,
                        flat_number=i[district]["flat_number"],
                        flat_average_price=i[district]["flat_average_price"],
                        flat_average_rent=None,
                        flat_m2_average_price=i[district]["flat_m2_average_price"],
                        date=date(given_date[2],given_date[1],given_date[0])
                    )
                        
                if "flat_average_price" in i:
                    try:
                        save_statistics_to_db(i,given_date=given_date)
                    except Exception as e:
                        save_statistics_to_db(i)
                else:
                    if "floor" in i:
                        if type(i['floor']) is list:
                            i['floor'] = i['floor'][0]

                    if "district" and "street" in i:
                        save_flat_to_db(i, i["district"], i["street"],given_date=given_date)
                    else:
                        save_flat_to_db(i, None, None,given_date=given_date)