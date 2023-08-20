#!/usr/bin/python3
"""
that contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

Base = declarative_base()


class City(Base):
    """
    class City
    inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
