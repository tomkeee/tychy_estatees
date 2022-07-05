import json,time

with open("otodom_02_07_2022.json", "r") as read_file:
    data = json.load(read_file)

    for i in data:
        print(i)
        print(len(i))

    # total_value = 0
    # total_value_known_space = 0

    # flat_number = 0

    # flat_unknown_price = 0

    # total_space = 0
    # flat_unknown_space = 0

    # for i in data:
        
    #     try:
    #         flat_price = i["price"]
    #     except:
    #         flat_price = None

    #     try:
    #         flat_space = i["space"]
    #     except:
    #         flat_space = None

    #     if flat_price and flat_space:
    #         flat_number += 1
    #         total_value += flat_price

    #         total_value_known_space += flat_price
    #         total_space += flat_space

    #     elif flat_price and not flat_space:
    #         flat_number += 1
    #         total_value += flat_price
    #         flat_unknown_space += 1

    #     elif flat_space and not flat_price:
    #         flat_number += 1
    #         flat_unknown_price += 1

    #     else:
    #         flat_unknown_price += 1
    #         flat_unknown_space += 1
    #         flat_number += 1

    # summary_data = {
    #     "flat number": flat_number,
    #     "average price": total_value / (flat_number - flat_unknown_price),
    #     "average m2 price": total_value_known_space / total_space,
    # }
