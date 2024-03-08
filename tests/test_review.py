#!/usr/bin/python3
"""Unit test for Review Model"""

from unittest import TestCase, main
from models.base_model import BaseModel
from models.review import Review

class TestState(TestCase):
"""Test review model"""

@classmethod
def setUp(cls):
"""setup class"""
cls.review = Review()
cls.review.place_id = "root_575"
cls.review.user_id = "kalix"
cls.review.text = "Some random good review"
cls.review.save()

def test_attr_place_id(self):
"""Test place_id attr"""
review_1 = Review()
self.assertEqual(self.review.place_id, "root_575")
self.assertIsInstance(self.review.place_id, str)
self.assertEqual(review_1.place_id, "")

def test_attr_user_id(self):
"""Test user_id attr"""
review_1 = Review()
self.assertEqual(self.review.user_id, "kalix")
self.assertIsInstance(self.review.user_id, str)
self.assertEqual(review_1.user_id, "")

def test_save_method(self):
"""Test save method"""
review_1 = Review()
review_1.save()
self.assertNotEqual(review_1.created_at, review_1.updated_at)

 def test_review_class(self):
"""instance should be review; review should
be a subclass of BaseModel"""
self.assertTrue(issubclass(Review, BaseModel))
self.assertIsInstance(self.review, Review)

@classmethod
def tearDownClass(cls):
"""Delete everything"""
del cls.review.place_id
del cls.review.user_id
del cls.review.text
del cls.review

if __name__ == "__main__":
        main()
                                            
                                            
