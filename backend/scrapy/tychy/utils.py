from .flat_schema import FlatSchema
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import json
from .models import Flat, Statistics, Streets, Districts
from datetime import date


def refer_value(reference, object):
    try:
        value = reference[object]
    except:
        value = None
    return value


def get_pydantic_model(reference, district, street):
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
        district=district,
        street=street,
    )
    return flat_pydantic


def save_flat_to_db(item, district, street,given_date=None):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        flat_pydantic = get_pydantic_model(item, district, street)
        if given_date:
            flat = Flat(**flat_pydantic.dict(), date=date(given_date[2],given_date[1],given_date[0]))
        else:
            flat = Flat(**flat_pydantic.dict(), date=date.today())
        session.add(flat)
        session.commit()
        session.refresh(flat)


def save_statistics_to_db(data,given_date=None):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        if given_date:
            stats = Statistics(**data, date=date(given_date[2],given_date[1],given_date[0]))
        else:
            stats = Statistics(**data, date=date.today())
        session.add(stats)
        session.commit()
        session.refresh(stats)


def save_streets_to_db(
    location=None,
    flat_number=None,
    flat_average_price=None,
    flat_average_rent=None,
    flat_m2_average_price=None,
    date=date.today()
):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        street_to_db = Streets(
            location=location,
            flat_number=flat_number,
            flat_average_price=flat_average_price,
            flat_average_rent=flat_average_rent,
            flat_m2_average_price=flat_m2_average_price,
            date=date,
        )
        session.add(street_to_db)
        session.commit()
        session.refresh(street_to_db)


def save_districts_to_db(
    location=None,
    flat_number=None,
    flat_average_price=None,
    flat_average_rent=None,
    flat_m2_average_price=None,
    is_district=False,
    is_street=False,
    date=date.today()
):
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        district_to_db = Districts(
            location=location,
            flat_number=flat_number,
            flat_average_price=flat_average_price,
            flat_average_rent=flat_average_rent,
            flat_m2_average_price=flat_m2_average_price,
            date=date,
        )
        session.add(district_to_db)
        session.commit()
        session.refresh(district_to_db)


def get_newest_flat():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        flat = session.query(Flat).order_by(Flat.date.desc()).first()

    return flat


def get_newest():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        stats = session.query(Statistics).order_by(Statistics.date.desc()).first()

    return stats


def get_newest_location_streets():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        street = session.query(Streets).order_by(Streets.date.desc()).first()
    return street


def get_newest_location_districts():
    with Session(
        create_engine("postgresql://postgres:postgres@database:5432/postgres")
    ) as session:
        district = session.query(Districts).order_by(Districts.date.desc()).first()
    return district


def add_dict_to_json(data, file):
    line = json.dumps(dict(data), ensure_ascii=False)
    file.write(line)

    new_line = "," + "\n"
    file.write(new_line)
