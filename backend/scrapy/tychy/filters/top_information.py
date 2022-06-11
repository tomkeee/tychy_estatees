from tychy.schemas import (
    FlatStatus,
    FlatFloor,
    FlatFormOfOwnership,
    FlatHeating,
    FlatMarket,
    AdvertiserType,
    TypeOfBuilding,
    TypeOfWindow,
    BuildingMaterial,
    MEDIA,
    ADDITIONALS,
)


def get_price(data):
    if data is None:
        return None

    values = []
    for s in data.split():
        s = s.replace(",", ".")
        try:
            z = int(s)
            values.append(s)
        except:
            s = s
    if len(values) >= 1:
        for i in range(len(values)):
            values[i] = str(values[i])
        numeric_value = int("".join(values))
    else:
        numeric_value = None
    return numeric_value


def get_number_of_rooms(data):
    if data is None:
        return None
    if data == "więcej niż 10":
        return 11

    for s in data.split():
        try:
            rooms_number = int(s)
            return rooms_number
        except:
            s = s
    return None


def get_flat_status(data):
    if data == "do zamieszkania":
        return FlatStatus.READY.value
    if data == "do wykończenia":
        return FlatStatus.FINISH.value
    if data == "do remontu":
        return FlatStatus.RENOVATION.value

    return FlatStatus.NOT_GIVEN.value


def get_flat_floor(data):
    if data is None:
        flat_floor = FlatFloor(flat_floor=None, all_floors=None, unique=None)
        flat_floor_dict = flat_floor.dict()
        return flat_floor_dict

    split_floors = data.split("/")
    if len(split_floors) != 2:
        flat_floor = FlatFloor(flat_floor=None, all_floors=None, unique=None)
        flat_floor_dict = flat_floor.dict()

        return flat_floor_dict

    if split_floors[0] == "parter":
        split_floors[0] = 0
    if split_floors[0] == "suterena" or split_floors[0] == "poddasze":
        flat_floor = FlatFloor(unique=split_floors[0], all_floors=int(split_floors[1]))
    else:
        if split_floors[0] == "> 10":
            split_floors[0] = 11
        flat_floor = FlatFloor(
            flat_floor=int(split_floors[0]), all_floors=int(split_floors[1])
        )

    flat_floor_dict = flat_floor.dict()
    return flat_floor_dict


def get_form_of_ownership(data):
    if data == "spółdzielcze własnościowe":
        return FlatFormOfOwnership.ASSOSCIATION.value
    if data == "spółdzielcze wł. z KW":
        return FlatFormOfOwnership.ASSOSCIATION_PB.value
    if data == "pełna własność":
        return FlatFormOfOwnership.FULL_PROPERTY.value
    if data == "udział":
        return FlatFormOfOwnership.SHARE.value
    return None


def get_flat_heating(data):
    if data == "miejskie":
        return FlatHeating.URBAN.value
    if data == "gazowe":
        return FlatHeating.GAS.value
    if data == "piece kaflowe":
        return FlatHeating.TILED_STOVE.value
    if data == "elektryczne":
        return FlatHeating.ELECTRIC.value
    if data == "kotłownia":
        return FlatHeating.BOILER_ROOM.value
    if data == "inne":
        return FlatHeating.DIFFERENT.value

    return None


def has_flat_car_park(data):
    if data == "garaż/miejsce parkingowe":
        return True
    else:
        return None


def get_flat_additionals(detail_field, inforamtion_field):
    additionals = []
    if detail_field is not None:
        detail_field = detail_field.replace(" ", "")
        detail_field = detail_field.split(",")
        for i in detail_field:
            if i in ADDITIONALS:
                additionals.append(i)

    if inforamtion_field is not None:
        inforamtion_field = inforamtion_field.replace(" ", "")
        inforamtion_field = inforamtion_field.split(",")
        for i in inforamtion_field:
            if i == "oddzielnakuchnia":
                additionals.append("oddzielna kuchnia")
                continue
            if i in ADDITIONALS:
                additionals.append(i)
    return additionals


def get_flat_market(data):
    if data == "wtórny":
        return FlatMarket.SECONDARY.value
    if data == "pierwotny":
        return FlatMarket.PRIMARY.value
    else:
        return None


def get_advertiser_type(data):
    if data is None:
        return None

    data = data.replace(" ", "")
    if data == "prywatny":
        return AdvertiserType.PRIVATE.value
    if data == "biuronieruchomości":
        return AdvertiserType.ESTATE_AGENCY.value


def get_type_of_building(data):
    if data == "blok":
        return TypeOfBuilding.BLOCK.value
    if data == "kamienica":
        return TypeOfBuilding.TENEMENT.value
    if data == "dom wolnostojący":
        return TypeOfBuilding.HOUSE.value
    if data == "plomba":
        return TypeOfBuilding.INFILL.value
    if data == "szeregowiec":
        return TypeOfBuilding.TOWNHOUSE.value
    if data == "apartamentowiec":
        return TypeOfBuilding.APARTAMENT.value
    if data == "loft":
        return TypeOfBuilding.LOFT.value
    return None


def has_flat_elevator(data):
    if data == "tak":
        return True
    if data == "nie":
        return False
    else:
        return None


def get_flat_window(data):
    if data == "plastikowe":
        return TypeOfWindow.PLASTIC.value
    if data == "drewniane":
        return TypeOfWindow.WOODEN.value
    if data == "aluminiowe":
        return TypeOfWindow.ALUMINIUM.value
    return None


def get_flat_media(data):
    if data is None:
        return None

    data = data.replace(" ", "")
    data_arr = data.split(",")

    media = []

    for i in range(len(data_arr)):
        if data_arr[i] == "telewizjakablowa":
            media.append("telewizja kablowa")
            continue

        if data_arr[i] in MEDIA:
            media.append(data_arr[i])
    return media


def get_build_year(data):
    try:
        build_year = int(data)
        return build_year
    except:
        return None


def get_building_material(data):
    if data == "cegła":
        return BuildingMaterial.BRICK.value
    if data == "drewno":
        return BuildingMaterial.WOOD.value
    if data == "pustak":
        return BuildingMaterial.BREEZEBLOCK.value
    if data == "keramzyt":
        return BuildingMaterial.HYDROTON.value
    if data == "wielka płyta":
        return BuildingMaterial.CONCRETE_PLATE.value
    if data == "silikat":
        return BuildingMaterial.SILIKAT.value
    if data == "beton komórkowy":
        return BuildingMaterial.CELLULAR_CONCRETE.value
    if data == "żelbet":
        return BuildingMaterial.REINFORCED_CONCRETE.value
    if data == "inne":
        return BuildingMaterial.OTHER.value
    return None
