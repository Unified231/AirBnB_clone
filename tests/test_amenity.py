#!/usr/bin/python3
"""Unit test for Amenity Model"""

from unittest import TestCase, main
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(TestCase):
"""Test amenity model"""

def test_attr_name(self):
"""Test name attr"""
amenity_1 = Amenity()
amenity_2 = Amenity()
amenity_1.name = "Kotlin"
self.assertEqual(amenity_1.name, "Kotlin")
self.assertIsInstance(amenity_1.name, str)
self.assertEqual(amenity_2.name, "")

def test_save_method(self):
"""Test save method"""
amenity_1 = Amenity()
amenity_1.save()
self.assertNotEqual(amenity_1.created_at, amenity_1.updated_at)

def test_amenity_class(self):
"""instance should be amenity; amenity
should be a subclass of BaseModel"""
amenity_1 = Amenity()
self.assertTrue(issubclass(type(amenity_1), BaseModel))
self.assertIsInstance(amenity_1, Amenity)

if __name__ == "__main__":
main()
