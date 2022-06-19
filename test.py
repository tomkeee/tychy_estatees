data = {
    "śródmieście": {
        "flats_number": 25,
        "flats_number_value": 25,
        "flats_value": 9051706,
        "flats_space": 1464.33,
        "flats_value_space": 9051706,
        "flats_number_space": 25,
    },
    "c": {
        "flats_number": 10,
        "flats_number_value": 10,
        "flats_value": 2981900,
        "flats_space": 497.92,
        "flats_value_space": 2981900,
        "flats_number_space": 10,
    },
    "mąkołowiec": {
        "flats_number": 7,
        "flats_number_value": 7,
        "flats_value": 3369000,
        "flats_space": 388.15999999999997,
        "flats_value_space": 3369000,
        "flats_number_space": 7,
    },
    "wilkowyje": {
        "flats_number": 13,
        "flats_number_value": 13,
        "flats_value": 5576647,
        "flats_space": 965.49,
        "flats_value_space": 5576647,
        "flats_number_space": 13,
    },
    "zwierzyniec": {
        "flats_number": 5,
        "flats_number_value": 3,
        "flats_value": 1422575,
        "flats_space": 306.57,
        "flats_value_space": 1422575,
        "flats_number_space": 3,
    },
    "b": {
        "flats_number": 16,
        "flats_number_value": 16,
        "flats_value": 4771000,
        "flats_space": 742.12,
        "flats_value_space": 4771000,
        "flats_number_space": 16,
    },
    "h": {
        "flats_number": 17,
        "flats_number_value": 17,
        "flats_value": 6626000,
        "flats_space": 981.4100000000001,
        "flats_value_space": 6626000,
        "flats_number_space": 17,
    },
    "żwaków": {
        "flats_number": 62,
        "flats_number_value": 62,
        "flats_value": 27399225,
        "flats_space": 3309.179999999999,
        "flats_value_space": 27399225,
        "flats_number_space": 62,
    },
    "paprocany": {
        "flats_number": 10,
        "flats_number_value": 10,
        "flats_value": 4760900,
        "flats_space": 763.5399999999998,
        "flats_value_space": 4760900,
        "flats_number_space": 10,
    },
    "cielmice": {
        "flats_number": 1,
        "flats_number_value": 1,
        "flats_value": 385000,
        "flats_space": 56.9,
        "flats_value_space": 385000,
        "flats_number_space": 1,
    },
    "urbanowice": {
        "flats_number": 3,
        "flats_number_value": 3,
        "flats_value": 1145900,
        "flats_space": 136.62,
        "flats_value_space": 1145900,
        "flats_number_space": 3,
    },
}

for i in data:
    data[i]["average_price"] = data[i]["flats_value"] / data[i]["flats_number_value"]
    data[i]["average_price_m2"] = data[i]["flats_value_space"] / data[i]["flats_space"]

print(data)


{
    "śródmieście": {
        "flats_number": 25,
        "flats_number_value": 25,
        "flats_value": 9051706,
        "flats_space": 1464.33,
        "flats_value_space": 9051706,
        "flats_number_space": 25,
        "average_price": 362068.24,
        "average_price_m2": 6181.465926396373,
    },
    "c": {
        "flats_number": 10,
        "flats_number_value": 10,
        "flats_value": 2981900,
        "flats_space": 497.92,
        "flats_value_space": 2981900,
        "flats_number_space": 10,
        "average_price": 298190.0,
        "average_price_m2": 5988.713046272494,
    },
    "mąkołowiec": {
        "flats_number": 7,
        "flats_number_value": 7,
        "flats_value": 3369000,
        "flats_space": 388.15999999999997,
        "flats_value_space": 3369000,
        "flats_number_space": 7,
        "average_price": 481285.71428571426,
        "average_price_m2": 8679.410552349547,
    },
    "wilkowyje": {
        "flats_number": 13,
        "flats_number_value": 13,
        "flats_value": 5576647,
        "flats_space": 965.49,
        "flats_value_space": 5576647,
        "flats_number_space": 13,
        "average_price": 428972.8461538461,
        "average_price_m2": 5775.975929320863,
    },
    "zwierzyniec": {
        "flats_number": 5,
        "flats_number_value": 3,
        "flats_value": 1422575,
        "flats_space": 306.57,
        "flats_value_space": 1422575,
        "flats_number_space": 3,
        "average_price": 474191.6666666667,
        "average_price_m2": 4640.294223179046,
    },
    "b": {
        "flats_number": 16,
        "flats_number_value": 16,
        "flats_value": 4771000,
        "flats_space": 742.12,
        "flats_value_space": 4771000,
        "flats_number_space": 16,
        "average_price": 298187.5,
        "average_price_m2": 6428.879426507842,
    },
    "h": {
        "flats_number": 17,
        "flats_number_value": 17,
        "flats_value": 6626000,
        "flats_space": 981.4100000000001,
        "flats_value_space": 6626000,
        "flats_number_space": 17,
        "average_price": 389764.70588235295,
        "average_price_m2": 6751.510581714064,
    },
    "żwaków": {
        "flats_number": 62,
        "flats_number_value": 62,
        "flats_value": 27399225,
        "flats_space": 3309.179999999999,
        "flats_value_space": 27399225,
        "flats_number_space": 62,
        "average_price": 441922.98387096776,
        "average_price_m2": 8279.762660236072,
    },
    "paprocany": {
        "flats_number": 10,
        "flats_number_value": 10,
        "flats_value": 4760900,
        "flats_space": 763.5399999999998,
        "flats_value_space": 4760900,
        "flats_number_space": 10,
        "average_price": 476090.0,
        "average_price_m2": 6235.298740079106,
    },
    "cielmice": {
        "flats_number": 1,
        "flats_number_value": 1,
        "flats_value": 385000,
        "flats_space": 56.9,
        "flats_value_space": 385000,
        "flats_number_space": 1,
        "average_price": 385000.0,
        "average_price_m2": 6766.256590509666,
    },
    "urbanowice": {
        "flats_number": 3,
        "flats_number_value": 3,
        "flats_value": 1145900,
        "flats_space": 136.62,
        "flats_value_space": 1145900,
        "flats_number_space": 3,
        "average_price": 381966.6666666667,
        "average_price_m2": 8387.498170106866,
    },
}