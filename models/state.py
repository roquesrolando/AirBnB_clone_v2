#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref='state')

    ''' Getter for cities '''
    @property
    def cities(self):
        ''' Returns the list of City instances
        with state_id equal to the current State.id '''
        temp = {}
        list_cities = []
        temp.update(FileStorage.__objects)
        for key, value in temp.items():
            if key.id == BaseModel.self.id
                if key.name != BaseModel.self.name:
                    list_cities.append(key.name)
        return list_cities


