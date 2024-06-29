#!/usr/bin/python3
""" A python module that defines a class definition of city
    a city
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ A class that defines a city
        Attributes:
            __tablename__ (str): The table name of the class
            id (int): id of each city
            name (str): name of cities
    """
    __tablename__ = "cities"
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True, unique=True, nullable=False
            )

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # Relationships
    state = relationship("State", back_populates="cities")
