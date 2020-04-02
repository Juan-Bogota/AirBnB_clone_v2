#!/usr/bin/python3

"""create a unique FileStorage instance for your application"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.engine import file_storage
from models.engine import db_storage

import os

if os.environ['HBNB_TYPE_STORAGE'] == "db":
    storage = db_storage.DBStorage()
else:
    storage = file_storage.FileStorage()

storage.reload()

#storage = FileStorage()
#storage.reload()
