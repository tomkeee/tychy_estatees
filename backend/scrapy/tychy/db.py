from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Flat, Statistics

with Session(
    create_engine("postgresql://postgres:postgres@database:5432/postgres")
) as session:
    session.query(Flat).delete()
    session.query(Statistics).delete()
    session.commit()


# with Session(
#     create_engine("postgresql://postgres:postgres@database:5432/postgres")
# ) as session:
#     flats = session.query(Flat)
#     for i in flats[-10:]:
#         print(i.floor)
