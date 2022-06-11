from typing import List, Optional
from xmlrpc.client import boolean
from pydantic import BaseModel


class additional(BaseModel):
    name: str


class FlatSchema(BaseModel):
    link: Optional[str] = None
    title: Optional[str] = None
    localization: Optional[str] = None
    price: Optional[int] = None
    rent: Optional[int] = None

    rooms: Optional[int] = None
    space: Optional[int] = None
    status: Optional[str]
    # floor : str = None
    ownership: Optional[str] = None

    heating: Optional[str]
    car_park: Optional[bool] = None
    market: Optional[str]
    advertiser_type: Optional[str]

    type_of_building: Optional[str]
    elevator: Optional[bool] = None
    flat_window: Optional[str]
    # flat_media
    build_year: Optional[int] = None

    additionals: Optional[List[additional]] = None

    building_material: Optional[str]
