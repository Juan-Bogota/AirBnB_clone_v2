#!/usr/bin/python3
"""This is the base model class for AirBnB"""

import uuid
import models
import os
from datetime import datetime

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """

    if os.environ['HBNB_TYPE_STORAGE'] == "db":

        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime(), nullable=False, default=datetime.now())
        updated_at = Column(DateTime(), nullable=False, default=datetime.now())


    def __init__(self, *args, **kwargs):
        """Instantiation of base model class
        """
        print('args   -->', args)
        print('kwargs   --> ', kwargs)
        if kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())


    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        if "_sa_instance_state" in my_dict:
            my_dict.pop("_sa_instance_state", None)

        return my_dict

    def delete(self):
        """ delete from the current database session obj if not None"""
        models.storage.delete(self.id)
