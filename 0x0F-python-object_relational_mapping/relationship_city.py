#!/usr/bin/python3
"""
contains the class definition of a City.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sys import argv


class City(Base):
    """
    class City
    inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
