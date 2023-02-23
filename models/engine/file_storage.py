#!/usr/bin/python3
"""Contains a class FileStorage"""
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{self.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        dictionary = {}
        with open(self.__file_path, 'w') as f:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                """this for loop utilise a key value pair to run
                    my_dict.items() and create a dictionary of key and value"""
                new_object = key.split('.')
                class_name = new_object[0]
                """new_object is equal to key.split('.')[0]
                    this split the key and take the first part of the key"""
                self.new(eval("{}".format(class_name))(**value))
                """this if statement is used to create a new object
                    with the class name of new_object and its value"""
        except FileNotFoundError:
            pass
