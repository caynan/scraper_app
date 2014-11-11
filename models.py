from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**settings.DATABASE))

DeclarativeBase = declarative_base()

def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Deals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    description = Column('link', String, nullable=True)
    location = Column('location', String, nullable=True)
    category = Column('category', String, nullable=True)
    original_price = Column('original_price', String, nullable=True)
    price = Column('price', String, nullable=True)
