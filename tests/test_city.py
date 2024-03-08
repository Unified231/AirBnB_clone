#!/usr/bin/python3
"""Unit test for City Model"""

from unittest import TestCase, main
from models.base_model import BaseModel
from models.city import City

class TestState(TestCase):
"""Test City model"""

 @classmethod
def setUp(cls):
"""setup class"""
cls.city = City()
cls.city.name = "root"
cls.city.state_id = "777"
cls.city.save()

def test_attr_name(self):
"""Test first name attr"""
city_1 = City()
self.assertEqual(self.city.name, "root")
self.assertIsInstance(self.city.name, str)
self.assertEqual(city_1.name, "")

def test_attr_state_id(self):
"""Test state_id attr"""
city_1 = City()
self.assertEqual(self.city.state_id, "777")
self.assertIsInstance(self.city.state_id, str)
self.assertEqual(city_1.state_id, "")

def test_save_method(self):
"""test save method"""
city_1 = City()
city_1.save()
self.assertNotEqual(city_1.created_at, city_1.updated_at)

def test_city_class(self):
"""instance should be City; city should be a subclass of BaseModel"""
self.assertTrue(issubclass(City, BaseModel))
self.assertIsInstance(self.city, City)

@classmethod
def tearDownClass(cls):
"""Delete everything"""
del cls.city.name
del cls.city

if __name__ == "__main__":
        main()
                                            
