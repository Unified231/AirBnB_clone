#!/usr/bin/env python3
"""This is the console for AirBnB"""

import cmd
from models import storage
from shlex import split  # split strings using shell syntax
import re as regex  # regular expressions

# NOTE: Just importing everything for the script
# NOTE: When the expression is evaluated it calls the models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
"""This class is the entry point of the command intepreter"""

prompt = "(hbnb)"

__all_classes = {
"BaseModel": BaseModel,
"User": User,
"State": State,
"City": City,
"Amenity": Amenity,
"Place": Place,
"Review": Review,
}

def do_quit(self, line):
"""Quit command to exit the program"""
return True

def do_EOF(self, line):
"""Quit command to exit the program at end of file"""
return True

def emptyline(self):
""" "Do nothing with empty lines"""
pass

def do_create(self, line):
"""Creates a new instance of specified class & saves it"""
my_list = self.split(line)
if line == "" or line is None:
print("** class name missing **")
else:
classname = my_list[0]
if classname not in self.__all_classes:
print("** class doesn't exist **")
return
obj = self.__all_classes[classname]()
obj.save()
print("{}".format(obj.id))

def do_show(self, line):
"""Prints the string representation of an instance"""
if line == "" or line is None:
print("** class name missing **")
else:
words = self.split(line)
if words[0] not in self.__all_classes:
print("** class doesn't exist **")
elif len(words) < 2:
print("** instance id missing **")
else:
key = "{}.{}".format(words[0], words[1])
if key not in storage.all():
print("** no instance found **")
else:
print(storage.all()[key])
def do_destroy(self, line):
"""Deletes an instance based on the class name and id"""
try:
if not line:
raise SyntaxError()
my_list = self.split(line)
if my_list[0] not in self.__all_classes:
raise NameError()
if len(my_list) < 2:
raise IndexError()
objects = storage.all()
key = my_list[0] + "." + my_list[1]
if key in objects:
del objects[key]
storage.save()
else:
raise KeyError()
except SyntaxError:
print("** class name missing **")
except NameError:
print("** class doesn't exist **")
except IndexError:
print("** instance id missing **")
except KeyError:
print("** no instance found **")

def do_all(self, line):
"""Prints all string representation of given instances"""
args = self.split(line)
my_list = []
objects = storage.all()
if line:
if args[0] not in self.__all_classes:
print("** class doesn't exist **")
return
objects = storage.all()
if not line:
objects = storage.all()
for key in objects:
my_list.append(objects[key])
print(my_list)
return
for key in objects:
name = key.split(".")
if name[0] == args[0]:
my_list.append(objects[key])
print(my_list)

 def do_update(self, line):
"""Updates an instance by adding or updating attributes"""
try:
if not line
raise SyntaxError()
my_list = self.split(line)
if my_list[0] not in self.__all_classes:
raise NameError()
if len(my_list) < 2:
raise IndexError()
objects = storage.all()
key = my_list[0] + "." + my_list[1]
if key not in objects:
raise KeyError()
if len(my_list) < 3:
raise AttributeError()
if len(my_list) < 4:
raise ValueError()
values = objects[key]
try:
values.__dict__[my_list[2]] = eval(my_list[3])
except Exception:
values.__dict__[my_list[2]] = my_list[3]
values.save()
except SyntaxError:
print("** class name missing **")
except NameError:
print("** class doesn't exist **")
except IndexError:
print("** instance id missing **")
except KeyError:
print("** no instance found **")
except AttributeError:
print("** attribute name missing **")
except ValueError:
print("** value missing **")

 def count(self, line):
"""count the number of instances of a class"""
counter = 0
try:
my_list = self.split(line)
if my_list[0] not in self.__all_classes:
raise NameError()
objects = storage.all()
for key in objects:
name = key.split(".")
if name[0] == my_list[0]:
counter += 1
print(counter)
except NameError:
print("** class doesn't exist **")

def strip_clean(self, args):
"""strips the argument and return a string of command
Args:
args: input list of args
Return:
returns string of arguments"""
new_list
new_list.append(args[0])
try:
my_dict = eval(args[1][args[1].find("{"): args[1].find("}") + 1])
except Exception:
my_dict = None
if isinstance(my_dict, dict):
new_str = args[1][args[1].find("(") + 1: args[1].find(")")]
new_list.append(((new_str.split(", "))[0]).strip('"'))
new_list.append(my_dict)
return new_list
new_str = args[1][args[1].find("(") + 1: args[1].find(")")]
new_list.append(" ".join(new_str.split(", ")))
return " ".join(i for i in new_list)

 def default(self, line):
""fetch all class instances and get the number of instance """
my_list = line.split(".")
if len(my_list) >= 2:
if my_list[1] == "all()":
self.do_all(my_list[0])
elif my_list[1] == "count()":
self.count(my_list[0])
elif my_list[1][:4] == "show":
self.do_show(self.strip_clean(my_list))
elif my_list[1][:7] == "destroy":
self.do_destroy(self.strip_clean(my_list))
elif my_list[1][:6] == "update":
args = self.strip_clean(my_list)
if isinstance(args, list):
key = args[0] + " " + args[1]
for k, v in args[2].items():
self.do_update(key + ' "{}" "{}"'.format(k, v))
else:
self.do_update(args)
else:
cmd.Cmd.default(self, line)

@staticmethod
def split(line):
return split(line)

if __name__ == "__main__":
HBNBCommand().cmdloop()
