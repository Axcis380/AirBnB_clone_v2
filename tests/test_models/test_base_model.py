#!/usr/bin/python3
"""Test module for BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import time


class test_basemodel(unittest.TestCase):
    """Test cases for BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instance creation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instance creation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instance creation with int kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test the save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test the string representation"""
        i = self.value()
        self.assertEqual(
            str(i),
            '[{}] ({}) {}'.format(self.name, i.id, i.__dict__)
        )

    def test_todict(self):
        """Test the dictionary representation"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instance creation with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instance creation with one kwargs"""
        n = {'unexpected_key': 'test'}
        new = self.value(**n)
        self.assertFalse(hasattr(new, 'unexpected_key'))

    def test_id(self):
        """Test the id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test the created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        new = self.value()
        old_updated_at = new.updated_at
        time.sleep(1)
        new.save()
        self.assertNotEqual(old_updated_at, new.updated_at)
