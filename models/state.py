#!/usr/bin/python3
"""This is the state class"""

import os

from models.base_model import BaseModel, Base
from models.city import City


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    """

    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              backref="state")
    else:
        cities = ""


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    if os.environ['HBNB_TYPE_STORAGE'] != "db":

        @property
        def cities(self):
            '''
            FileStorage to return City
            instances with state_id == current State.id
            '''
            list_cities = []
            for city_instance in models.storage.all(City).values():

                if city_instance.state_id == self.id:
                    list_cities.append(city_instance)

                    return list_cities
