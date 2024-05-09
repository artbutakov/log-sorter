from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.settings import database_settings as dbs

# from web import app

Base = declarative_base()


engine = create_engine(
    URL.create(
        drivername='postgresql+psycopg2',
        username=dbs.username,
        password=dbs.password.get_secret_value(),
        database=dbs.name,
    ),
    enable_from_linting=False,
)
session_maker = sessionmaker(bind=engine)


def drop_database():
    Base.metadata.drop_all(bind=engine)


def initiate_database():
    Base.metadata.create_all(bind=engine)
