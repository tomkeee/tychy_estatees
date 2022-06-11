from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@database:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
