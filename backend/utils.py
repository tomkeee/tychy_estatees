import json

from os import listdir
from os.path import isfile, join

from scrapy.tychy.utils import save_flat_to_db,save_statistics_to_db

mypath = "/code/data"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

json_files = list()


def save_spaces():
    iteration = 0
    for file in onlyfiles:
        iteration += 1
        print(iteration)
        if file.endswith(".json"):
            with open(str(mypath+"/"+ file), "r") as read_file:
                data = json.load(read_file)

                new_value = file.split("_")
                given_date = []

                given_date.append(int(new_value[1]))
                given_date.append(int(new_value[2]))
                given_date.append(int(new_value[3].replace(".json","")))

                for i in data:
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

                        

                

save_spaces()
