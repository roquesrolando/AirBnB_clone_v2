#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from os import getenv

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref='state')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            ''' Returns the list of City instances
            with state_id equal to the current State.id '''
            temp = storage.all(City)
            list_cities = []
            for city in temp.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
