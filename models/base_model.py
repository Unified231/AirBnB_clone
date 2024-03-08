#!/usr/bin/python3
"""This is the base model class for AirBnB Clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
"""This class defines common methods for other classes"""
def __init__(self, *args, **kwargs):
"""Instantiation of base model class
Args:
args: it won't be used
kwargs: arguments for the constructor of the BaseModel
Attributes:
id: unique id generated
created_at: creation date
updated_at: updated date"""
if kwargs:
for key, value in kwargs.items():
if key == "created_at" or key == "updated_at":
value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
if key != "__class__":
setattr(self, key, value)
if "id" not in kwargs.keys():
setattr(self, "id", str(uuid.uuid4()))
time = datetime.now()
if "created_at" not in kwargs.keys():
setattr(self, "created_at", time)
if "updated_at" not in kwargs.keys():
setattr(self, "updated_at", time)
else:
self.id = str(uuid.uuid4())
self.created_at = datetime.now()
self.updated_at = self.created_at
models.storage.new(self)
def __str__(self):
"""returns a string
Return:
returns a string of class name, id, and dictionary"""
dic = self.to_dict()
return "[{}] ({}) {}".format(type(self).__name__, self.id, 
def __repr__(self):
"""return a string representaion"""
return self.__str__(self)
def save(self):
"""updates the public instance attribute updated_at to current"""
self.updated_at = datetime.now()
models.storage.new(self)
models.storage.self
def to_dict(self):
"""creates dictionary of the class  and returns
Return:
returns a dictionary of all the key values in __dict__"""
my_dict = self.__dict__.copy()
my_dict["__class__"] = type(self).__name__
my_dict["created_at"] = my_dict["created_at"].isoformat()
my_dict["updated_at"] = my_dict["updated_at"].isoformat()
if "_sa_instance_state" in my_dict.keys():
my_dict.pop("_sa_instance_state", None)
return my_dict

# NOTE: Implement delete function later
"""def delete(self):
""Delete the current instance from the storage
 (models.storage) by calling the method delete""
 models.storage.delete(self)"""
