#!/usr/bin/python3

"""
Unit test for BaseModel
"""
from unittest import TestCase, main
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel_Attr(TestCase):
"""Test the Base Model Instances"""

 def test_none_id(self):
"""Test unique id attribute is not null"""
model_1 = BaseModel()
model_2 = BaseModel()
self.assertIsNot(model_1.id, None)
self.assertIsNot(model_2.id, None)

def test_creation_date(self):
"""Test creation date attribute"""
model_1 = BaseModel()
model_2 = BaseModel()
model_1.created_at = datetime.now()
mock_date = model_1.created_at
self.assertEqual(model_1.created_at, mock_date)
self.assertNotEqual(model_1.created_at, model_2.created_at)

def test_update_date(self):
"""Test update date attribute"""
model_1 = BaseModel()
mock_date = model_1.created_at
self.assertEqual(model_1.updated_at, mock_date)

def test_base_model_attr_instance(self):
"""Test the Base Model attributes instances"""
model_1 = BaseModel()
self.assertIsInstance(model_1.id, str)
self.assertIsInstance(model_1.created_at, datetime)
self.assertIsInstance(model_1.updated_at, datetime)

class TestBaseModel_Str(TestCase):
"""Test string attributes for the BaseModel class"""

def test_str_attr_case(self):
"""Test if __str__ produces a string"""
model_1 = BaseModel()
self.assertEqual(type(model_1.__str__()), str)

def test_str_case(self):
"""Test if __str__ normal case"""
model_1 = BaseModel()
string = "[{}] ({}) {}".format(
model_1.__class__.__name__, model_1.id, model_1.to_dict()
)
self.assertEqual(model_1.__str__(), string)

def test_mismatched_str_type_case(self):
"""Test mismatched __str__ type case"""
model_1 = BaseModel()
string = "[{}] ({}) {}".format(
model_1.__class__.__name__, model_1.id, model_1.__dict__
)
self.assertNotEqual(model_1.__str__(), string)

 def test_string_repr(self):
"""Test the string representation type"""
model_1 = BaseModel()
self.assertEqual(type(model_1.__repr__()), str)
self.assertIsInstance(model_1.__str__(), str)


class TestBaseModel_Dict(TestCase):
"""Test to_dict attributes for BaseModel Class"""

def test_to_dict_normal_case(self):
"""Normal use case for to_dict"""
model_1 = BaseModel()
dict_value = model_1.to_dict()
self.assertDictEqual(dict_value, model_1.to_dict())

def test_dict_attr_case(self):
"""Test the attribute for to_dict"""
model_1 = BaseModel()
self.assertEqual(type(model_1.to_dict()), dict)

def test_to_dict_instance(self):
"""Test the to_dict instance"""
model_1 = BaseModel()
self.assertIsInstance(model_1.to_dict(), dict)

class TestBaseModel_Save(TestCase):
        """Test the save method of the class"""

def test_normal_case(self):
"""Test save method with updated date"""
model_1 = BaseModel()
tmp_date = model_1.updated_at
model_1.save()
# NOTE: Just to make sure dates are not the same
self.assertNotEqual(model_1.updated_at, tmp_date)

if __name__ == "__main__":
        main()


