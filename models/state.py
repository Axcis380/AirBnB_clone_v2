#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        # For DBStorage: relationship with the class City
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan"
                              )
    else:
        name = ""

        @property
        def cities(self):
            """FileStorage relationship between State and City."""
            from models import storage
            file_cities = storage.all(storage.classes['City']).values()
            return [city for city in file_cities if city.state_id == self.id]
