#!/usr/bin/python3

"""
This module handles the instances of the Storage Engine
"""

import json


class FileStorage:
"""FileStorage class that handles read/write instances
Attributes:
__file_path (file): file to work with
__objects (obj): Json Object"""

__file_path = "file.json"
__objects = dict()

def all(self):
"""Return dictionary __objects with no specific 
Return:
Brings all the objects in storage"""
return self.__objects
def new(self, obj):
"""Creates a new object with key
Args:
self: self
obj (obj): The object to work with"""
obj_key = "{}.{}".format(obj.__class__.__name__, obj.id)
self.__objects[obj_key] = obj

def save(self):
"""Saves the object blob to File Storage 
new_obj is a dictionary format for the object storage"""
new_obj = {key: values.to_dict()
for key, values in self.__objects.items()}
with open(self.__file_path, "w", encoding="utf8") as file:
file.write(json.dumps(new_object))
def reload(self):
"""This loads objects from the specified file.
If not present still pass the function"""

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# NOTE: Bring models for list comparison
class_dict = {
"BaseModel": BaseModel,
"User": User,
"State": State,
"City": City,
"Amenity": Amenity,
"Place": Place,
"Review": Review,
}

try:
with open(self.__file_path, "r") as file:
self.__objects = json.load(file)
for value in self.__objects.values():
class_name = value["__class__"]
del value["__class__"]
if class_name in class_dict:
self.new(class_dict[class_name](**value))
except FileNotFoundError:
pass
return self.__objects
