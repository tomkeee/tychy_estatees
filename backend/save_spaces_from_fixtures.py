import json
from datetime import date
from os import listdir
from os.path import isfile, join

from scrapy.tychy.utils import save_flat_to_db,save_statistics_to_db,save_streets_to_db,save_districts_to_db

mypath = "/code/data"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

json_files = list()


iteration = 0
for file in onlyfiles:
    iteration += 1
    print(f"{iteration} out of {len(onlyfiles)}")
    if file.endswith(".json"):
        with open(str(mypath+"/"+ file), "r") as read_file:
            data = json.load(read_file)

            new_value = file.split("_")
            given_date = []

            given_date.append(int(new_value[1]))
            given_date.append(int(new_value[2]))
            given_date.append(int(new_value[3].replace(".json","")))

            for i in data:
                if "bielska" in list(i.keys()):
                    for street in i:
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