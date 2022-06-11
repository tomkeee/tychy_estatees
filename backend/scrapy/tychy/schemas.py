from enum import Enum
from typing import Optional
from pydantic import BaseModel

MEDIA = ("telewizjakablowa", "internet", "telefon")

ADDITIONALS = (
    "balkon",
    "piwnica",
    "ogródek",
    "taras",
    "oddzielnakuchnia",
    "dwupoziomowe",
    "klimatyzacja",
)


class FlatStatus(Enum):
    RENOVATION = "renovation"
    READY = "ready"
    FINISH = "finish"
    NOT_GIVEN = None


class FlatFloor(BaseModel):
    flat_floor: Optional[int]
    all_floors: Optional[int]
    unique: Optional[str]


class FlatFormOfOwnership(Enum):
    ASSOSCIATION = "housing assosciation"
    ASSOSCIATION_PB = "housing assosciation - ownership by perpetual book"
    FULL_PROPERTY = "full property"
    SHARE = "share"


class FlatHeating(Enum):
    URBAN = "urban heating"
    GAS = "Gas heating"
    TILED_STOVE = "tiled stove heating"
    ELECTRIC = "electric heating"
    BOILER_ROOM = "boiler room heating"
    DIFFERENT = "different"


class FlatMarket(Enum):
    PRIMARY = "primary market"
    SECONDARY = "secondary market"


class AdvertiserType(Enum):
    PRIVATE = "private"
    ESTATE_AGENCY = "estate agency"


class TypeOfBuilding(Enum):
    BLOCK = "blok"
    TENEMENT = "kamienica"
    HOUSE = "house"
    INFILL = "infill"
    TOWNHOUSE = "town house"
    APARTAMENT = "apartment"
    LOFT = "loft"


class TypeOfWindow(Enum):
    PLASTIC = "plastic"
    WOODEN = "wooden"
    ALUMINIUM = "aluminium"


class BuildingMaterial(Enum):
    BRICK = "brick"
    WOOD = "wood"
    BREEZEBLOCK = "breezeblock"
    HYDROTON = "hydroton"
    CONCRETE_PLATE = "concrete plate"
    CONCRETE = "concrete"
    SILIKAT = "silikat"
    CELLULAR_CONCRETE = "cellular concrete"
    REINFORCED_CONCRETE = "reinforced concrete"
    OTHER = "other"
