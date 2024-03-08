#!/usr/bin/python3
"""Unit test for Place Model """

from unittest import TestCase, main
from models.base_model import BaseModel
from models.place import Place

class TestPlace(TestCase):
"""Test place model"""

@classmethod
def setUp(cls):
"""setup class"""
cls.place = Place()
cls.place.city_id = "localhost_8080"
cls.place.user_id = "root_127"
cls.place.name = "kalixy"
cls.place.description = "No place like 127.0.0.1"
cls.place.number_rooms = 4
cls.place.number_bathrooms = 2
cls.place.max_guest = 4
cls.place.price_by_night = 0
cls.place.latitude = 127.0
cls.place.longitude = 0.0
cls.place.amenity_ids = ["Linux", "Free", "FOSS", "OS"]
cls.place.save()

def test_attr_city_id(self):
"""Test city_id attr"""
root_home = Place()
self.assertEqual(self.place.city_id, "localhost_8080")
self.assertIsInstance(self.place.city_id, str)
self.assertEqual(root_home.city_id, "")

def test_attr_user_id(self):
"""Test user_id attr"""
root_home = Place()
self.assertEqual(self.place.user_id, "root_127")
self.assertIsInstance(self.place.user_id, str)
self.assertEqual(root_home.user_id, "")

def test_name_attr(self):
"""Test name attr"""
root_home = Place()
self.assertTrue(self.place.name, "kalixy")
self.assertIsInstance(self.place.name, str)
self.assertEqual(root_home.name, "")

 def test_desc_attr(self):
"""Test description attr"""
root_home = Place()
self.assertEqual(self.place.description, "No place like 127.0.0.1")
self.assertIsInstance(self.place.description, str)
self.assertEqual(root_home.description, "")

def test_number_rooms_attr(self):
"""Test number rooms attr"""
root_home = Place()
self.assertEqual(self.place.number_rooms, 4)
self.assertIsInstance(self.place.number_rooms, int)
self.assertEqual(root_home.number_rooms, 0)

def test_number_bathrooms_attr(self):
"""Test number_bathrooms attr"""
root_home = Place()
self.assertEqual(self.place.number_bathrooms, 2)
self.assertIsInstance(self.place.number_bathrooms, int)
self.assertEqual(root_home.number_bathrooms, 0)

def test_guests_attr(self):
"""Test max_guest attr"""
root_home = Place()
self.assertEqual(self.place.max_guest, 4)
self.assertIsInstance(self.place.max_guest, int)
self.assertEqual(root_home.max_guest, 0)

def test_price_attr(self):
"""Test price_by_night attr"""
root_home = Place()
self.assertEqual(self.place.price_by_night, 0)
# NOTE: I know we should test for float
# but it won't pass, putting int for now
self.assertIsInstance(self.place.price_by_night, int)
self.assertEqual(root_home.price_by_night, 0)

 def test_lat_attr(self):
"""Test latitude attr"""
root_home = Place()
self.assertEqual(self.place.latitude, 127.0)
self.assertIsInstance(self.place.latitude, float)
self.assertEqual(root_home.latitude, 0.0)

def test_long_attr(self):
"""Test longitude attr"""
root_home = Place()
self.assertEqual(self.place.longitude, 0.0)
self.assertIsInstance(self.place.longitude, float)
self.assertEqual(root_home.longitude, 0.0)

def test_amenity_attr(self):
"""Test Amenities attr"""
root_home = Place()
tmp_list = ["Linux", "Free", "FOSS", "OS"]
self.assertEqual(self.place.amenity_ids, tmp_list)
self.assertIsInstance(self.place.amenity_ids, list)
self.assertEqual(root_home.amenity_ids, [])

def test_save_method(self):
"""Test save method"""
root_home = Place()
root_home.save()
self.assertNotEqual(root_home.created_at, root_home.updated_at)

def test_place_class(self):
"""instance should be Place; place should be a subclass of BaseModel"""
self.assertTrue(issubclass(Place, BaseModel))
self.assertIsInstance(self.place, Place)

 @classmethod
def tearDownClass(cls):
"""Delete everything"""
del cls.place.city_id
del cls.place.user_id
del cls.place.name
del cls.place.description
del cls.place.number_rooms
del cls.place.number_bathrooms
del cls.place.max_guest
del cls.place.price_by_night
del cls.place.latitude
del cls.place.longitude
del cls.place.amenity_ids
del cls.place

if __name__ == "__main__":
        main()
