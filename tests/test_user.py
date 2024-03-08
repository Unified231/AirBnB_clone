#!/usr/bin/python3
"""Unit test for User Model """

from unittest import TestCase, main
from models.base_model import BaseModel
from models.user import User

class TestUser(TestCase):
"""Test user model"""

@classmethod
def setUp(cls):
"""setup class"""
cls.user = User()
cls.user.first_name = "root"
cls.user.last_name = "toor"
cls.user.email = "root@kali.com"
cls.user.password = "kali"
cls.user.save()

def test_attr_first_name(self):
"""Test first name attr"""
root_user = User()
self.assertEqual(self.user.first_name, "root")
self.assertIsInstance(self.user.first_name, str)
self.assertEqual(root_user.first_name, "")

def test_attr_last_name(self):
"""Test last name attr"""
root_user = User()
self.assertEqual(self.user.password, "kali")
self.assertIsInstance(self.user.password, str)
self.assertEqual(root_user.password, "")

 def test_attr_email(self):
"""Test email attr"""
root_user = User()
self.assertTrue(self.user.email, "root@kali.com")
self.assertIsInstance(self.user.email, str)
self.assertEqual(root_user.email, "")

def test_attr_password(self):
"""Test password attr"""
root_user = User()
self.assertEqual(self.user.last_name, "toor")
self.assertIsInstance(self.user.last_name, str)
self.assertEqual(root_user.last_name, "")

def test_save_method(self):
"""Test save method"""
root_user = User()
root_user.save()
self.assertNotEqual(root_user.created_at, root_user.updated_at)

def test_user_class(self):
"""instance should be User; user should be a subclass of BaseModel"""
self.assertTrue(issubclass(User, BaseModel))
self.assertIsInstance(self.user, User)

@classmethod
def tearDownClass(cls):
"""Delete everything"""
del cls.user.first_name
del cls.user.last_name
del cls.user.email
del cls.user.password
del cls.user

if __name__ == "__main__":
        main()
                                                        
                                             

