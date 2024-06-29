#!/usr/bin/python3
""" A script that creates a class
    definition of a State, which will be translated
    to a MySQL database table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ A class definition of a State """
    __tablename__ = 'states'

    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            unique=True,
            nullable=False
            )
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
