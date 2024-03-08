#!/usr/bin/python3
"""Unit test for State Model"""

from unittest import TestCase, main
from models.base_model import BaseModel
from models.state import State

class TestState(TestCase):
"""Test state model"""

@classmethod
def setUp(cls):
"""setup class"""
cls.state = State()
cls.state.name = "root_767"
cls.state.save()

def test_attr_name(self):
"""Test name attr"""
state_1 = State()
self.assertEqual(self.state.name, "root_767")
self.assertIsInstance(self.state.name, str)
self.assertEqual(state_1.name, "")

def test_save_method(self):
"""Test save method"""
state_1 = State()
state_1.save()
self.assertNotEqual(state_1.created_at, state_1.updated_at)

def test_state_class(self):
"""instance should be state; state should be a subclass of BaseModel"""
self.assertTrue(issubclass(State, BaseModel))
self.assertIsInstance(self.state, State)

 @classmethod
def tearDownClass(cls):
"""Delete everything"""
del cls.state.name
del cls.state

if __name__ == "__main__":
        main()
                                    
