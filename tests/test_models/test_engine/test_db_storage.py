#!/usr/bin/python3
"""
This module contains the unit tests for the DBStorage class
"""

import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class TestDBStorage(unittest.TestCase):
    """Define tests for the DBStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test suite"""
        cls.engine = create_engine('sqlite:///:memory:')
        cls.DBStorage = DBStorage()
        cls.DBStorage._DBStorage__engine = cls.engine
        cls.DBStorage.reload()

    @classmethod
    def tearDownClass(cls):
        """Tear down after tests"""
        cls.DBStorage.close()

    def test_initialization(self):
        """Test initialization of DBStorage"""
        self.assertIsInstance(self.DBStorage, DBStorage)


if __name__ == "__main__":
    unittest.main()
