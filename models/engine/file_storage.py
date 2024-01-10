#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        If cls is provided, it returns only objects of that class.
        """
        if cls:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    cls_name = val['__class__']
                    if cls_name in [User, Place, State, City, Amenity, Review]:
                        self.new(eval(cls_name)(**val))
        except FileNotFoundError:
            pass
