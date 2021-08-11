#!/usr/bin/python3
"""Storage of MySQL"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.state import State
from models.city import City


class DBStorage:
    """ Database based system"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor for DB"""

        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """returns all objects of the class"""

        dict_o = {}
        if cls is not None:
            objects = self.__session.query(cls)
        for obj in objects:
            print(obj)
            key = obj.__class__.__name__ + '.' + obj.id
            dict_o[key] = obj
        return dict_o

    def new(self, obj):
        """add the object to the database"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """commit the changes to the database"""

        self.__session.commit()

    def delete(self, obj=None):
        """deletes objects from the database"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates datasabe from the engine"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
