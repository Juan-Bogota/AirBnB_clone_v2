#!/usr/bin/python3
"""
This module contains one class DBStorage.
This module deals with storing and
retrieving data from a mysql database.
"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    """doc
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        initializes engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        # adding, echo=True) shows SQL statements

        if getenv('HBNB_ENV', 'not') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__models_available = {"State": State,
                                   "City": City,
                                   #"Amenity": Amenity,
                                   #"Place": Place,
                                   #"Reivew": Review,
                                   #"User": User,
        }


    def all(self, cls=None):
        """
        returns a dictionary of all the class objects
        """
        print('cls --> ', cls)
        my_dict = {}
        if cls is None:
            for model in self.__models_available.values():

                if self.__session.query(model).all():
                    for item in self.__session.query(model).all():
                        my_dict[item.id] = item
        else:
            for item in self.__session.query(self.__models_available[cls]):
                my_dict[item.id] = item

        return my_dict

    def new(self, obj):
        """
        adds a new obj to the session
        """
        self.__session.add(obj)


    def save(self):
        """
        saves the objects fom the current session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes an object from the current session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """doc
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        close a session
        """
        self.__session.remove()
