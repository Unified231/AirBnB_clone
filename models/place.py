#!/usr/bin/python3
""" Place class """

from models.base_model import BaseModel


class Place(BaseModel):
"""Place class
Attributes:
city_id (string): the city id
user_id (string): the user id (who registered the place)
name (string): the name of user
description (string): description of the place
number_rooms (integer): number of rooms available
number_bathrooms (integer): number of bathrooms available
max_guest (integer): max number of guests
price_by_night (float): the price of room per night
latitude (float): latitude coordinates
longitude (float): longitude coordinates
amenity_ids (list): list of amenities available"""

city_id = ""
user_id = ""
name = ""
description = ""
number_rooms = 0
number_bathrooms = 0
max_guest = 0
price_by_night = 0
latitude = 0.0
longitude = 0.0
amenity_ids = []
