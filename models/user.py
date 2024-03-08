#!/usr/bin/python3
""" User class """

from models.base_model import BaseModel


class User(BaseModel):
"""User class
Attributes:
email (string): User email address
password (string): User password
first_name (string): User name
last_name (string): User surname"""

email = ""
password = ""
first_name = ""
last_name = ""
