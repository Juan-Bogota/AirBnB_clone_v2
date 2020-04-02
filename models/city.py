#!/usr/bin/python3
"""This is the city class"""

from models.base_model import BaseModel, Base

import os

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class City(BaseModel, Base):
    """This is the class for City
    """
    if os.environ['HBNB_TYPE_STORAGE'] == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
