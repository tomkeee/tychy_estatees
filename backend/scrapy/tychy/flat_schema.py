from typing import List, Optional
from xmlrpc.client import boolean
from pydantic import BaseModel, validator


class additionals(BaseModel):
    name: str


class FlatSchema(BaseModel):
    link: Optional[str] = None
    title: Optional[str] = None
    localization: Optional[str] = None
    price: Optional[int] = None
    rent: Optional[int] = None

    rooms: Optional[int] = None
    space: Optional[float] = None
    status: Optional[str]
    # floor : str = None
    ownership: Optional[str] = None

    heating: Optional[str]
    car_park: Optional[boolean] = None
    market: Optional[str]
    advertiser_type: Optional[str]

    type_of_building: Optional[str]
    elevator: Optional[boolean] = None
    flat_window: Optional[str]
    flat_media: Optional[List[str]] = None
    build_year: Optional[int] = None
    building_material: Optional[str]
    floor: Optional[dict] = None
    additionals: Optional[List[str]] = None

    @validator("additionals", pre=True, each_item=True)
    def additionals_each_element_should_be_a_string(cls, add_list):
        additionals_as_string = ""
        is_first = True

        for i in add_list:
            if is_first:
                additionals_as_string += str(i)
            else:
                additionals_as_string += "," + str(i)

        return additionals_as_string

    @validator("flat_media", pre=True, each_item=True)
    def flat_media_each_element_should_be_a_string(cls, media_list):
        flat_media = ""
        is_first = True

        for i in media_list:
            if is_first:
                flat_media += i
            else:
                flat_media += "," + i

        return flat_media
