from .flat_schema import FlatSchema
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from .models import Flat, Statistics
from datetime import date


def refer_value(reference, object):
    try:
        value = reference[object]
    except:
        value = None
    return value


def get_pydantic_model(reference):
    link = refer_value(reference, "link")
    title = refer_value(reference, "title")
    localization = refer_value(reference, "localization")
    price = refer_value(reference, "price")
    rent = refer_value(reference, "rent")
    rooms = refer_value(reference, "rooms")
    space = refer_value(reference, "space")
    status = refer_value(reference, "status")
    floor = refer_value(reference, "floor")
    ownership = refer_value(reference, "ownership")
    heating = refer_value(reference, "heating")
    car_park = refer_value(reference, "car_park")
    market = refer_value(reference, "market")
    advertiser_type = refer_value(reference, "advertiser_type")
    type_of_building = refer_value(reference, "type_of_building")
    elevator = refer_value(reference, "elevator")
    flat_window = refer_value(reference, "flat_window")
    flat_media = refer_value(reference, "flat_media")
    build_year = refer_value(reference, "build_year")
    building_material = refer_value(reference, "building_material")
    additionals = refer_value(reference, "additionals")

    flat_pydantic = FlatSchema(
        link=link,
        title=title,
        localization=localization,
        price=price,
        rent=rent,
        rooms=rooms,
        space=space,
        status=status,
        floor=floor,
        ownership=ownership,
        heating=heating,
        car_park=car_park,
        additionals=additionals,
        market=market,
        advertiser_type=advertiser_type,
        type_of_building=type_of_building,
        elevator=elevator,
        flat_window=flat_window,
        flat_media=flat_media,
        build_year=build_year,
        building_material=building_material,
    )
    return flat_pydantic


def save_flat_to_db(item):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        flat_pydantic = get_pydantic_model(item)
        flat = Flat(**flat_pydantic.dict(), date=date.today())
        session.add(flat)
        session.commit()
        session.refresh(flat)


def save_statistics_to_db(data):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        stats = Statistics(**data, date=date.today())
        session.add(stats)
        session.commit()
        session.refresh(stats)


def get_newest_flat():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        flat = session.query(Flat).order_by(Flat.date.desc()).first()

    return flat


def get_newest_stats():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        stats = session.query(Statistics).order_by(Statistics.date.desc()).first()

    return stats
