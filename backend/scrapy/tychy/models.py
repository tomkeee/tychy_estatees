from xmlrpc.client import Boolean
from .database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    PickleType,
    Date,
    ForeignKey,
)
from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy.orm import relationship


class Flat(Base):
    __tablename__ = "tychy_flat"
    id = Column(Integer(), primary_key=True)

    link = Column(String(300), nullable=True)
    title = Column(String(300), nullable=True)
    localization = Column(String(300), nullable=True)
    price = Column(Integer(), nullable=True)
    rent = Column(Integer(), nullable=True)

    rooms = Column(Integer(), nullable=True)
    space = Column(Float(), nullable=True)
    status = Column(String(300), nullable=True)
    floor = Column(PickleType)
    ownership = Column(String(300), nullable=True)

    heating = Column(String(300), nullable=True)
    car_park = Column(Boolean, nullable=True)
    market = Column(String(300), nullable=True)
    advertiser_type = Column(String(300), nullable=True)
    type_of_building = Column(String(300), nullable=True)

    elevator = Column(Boolean, nullable=True)
    flat_window = Column(String(300), nullable=True)
    flat_media = Column(String(3000), nullable=True)
    build_year = Column(Integer(), nullable=True)
    building_material = Column(String(300), nullable=True)

    additionals = Column(String(3000), nullable=True)

    district = Column(String(3000), nullable=True)
    street = Column(String(3000), nullable=True)

    date = Column(Date(), nullable=True)

    picture = image_attachment("FlatPicture")


class Statistics(Base):
    __tablename__ = "flats_statistics"
    id = Column(Integer(), primary_key=True)
    flat_number = Column(Integer(), nullable=True)
    flat_average_price = Column(Float(), nullable=True)
    flat_average_rent = Column(Float(), nullable=True)
    flat_m2_average_price = Column(Float(), nullable=True)
    date = Column(Date(), nullable=True)


class Districts(Base):
    __tablename__ = "flats_districts"
    id = Column(Integer(), primary_key=True)
    location = Column(String(3000), nullable=True)
    flat_number = Column(Integer(), nullable=True)
    flat_average_price = Column(Float(), nullable=True)
    flat_average_rent = Column(Float(), nullable=True)
    flat_m2_average_price = Column(Float(), nullable=True)
    date = Column(Date(), nullable=True)


class Streets(Base):
    __tablename__ = "flats_streets"
    id = Column(Integer(), primary_key=True)
    location = Column(String(3000), nullable=True)
    flat_number = Column(Integer(), nullable=True)
    flat_average_price = Column(Float(), nullable=True)
    flat_average_rent = Column(Float(), nullable=True)
    flat_m2_average_price = Column(Float(), nullable=True)
    date = Column(Date(), nullable=True)


class FlatPicture(Base, Image):
    """User picture model."""

    flat_id = Column(Integer, ForeignKey("tychy_flat.id"), primary_key=True)
    flat = relationship("Flat")
    __tablename__ = "flat_picture"
