#!/usr/bin/python3
"""
Amenity Module for HBNB project
This module defines the Amenity class, representing the amenities available
in the HBNB project. It supports both database storage and file storage
with appropriate relationships and attributes.
"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity
import os


class Amenity(BaseModel, Base):
    """
    Represents an Amenity for the HBNB project.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store amenities.
        name (sqlalchemy.Column): The name of the amenity.
        place_amenities : A relationship between places and amenities.
    """

    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        # Many-to-Many relationship with Place
        place_amenities = relationship('Place',
                                       back_populates='amenities',
                                       secondary=place_amenity
                                       )
    else:
        name = ""
