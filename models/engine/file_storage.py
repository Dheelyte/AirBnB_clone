#!/usr/bin/python3
"""Contains a class FileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Class FileStorage that serializes and deserializes
    instances to JSON
        __file_path: the path of the JSON file
        __objects: a dictionary of all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
            dicttionary: an empty dictionnary
            Open the dictionary in write mode
            dump the dictionary in the file f
        """
        objects = FileStorage.__objects
        objdict = {obj: objects[obj].to_dict() for obj in objects.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
            otherwise, do nothing.
            If the file doesn’t exist, no exception should be raised)
            Open in read mode"
            load the file f and read it"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
