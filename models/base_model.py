#!/usr/bin/python3
"""This file constains a Base model called BaseModel"""
from datetime import datetime
import uuid

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """ Instantiates a new object
            Args:
                *args: list of arguments
                **kwargs: (key - value) pair of attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save method for saving object instances"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return object instance attributes as dict"""
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat(sep='T')
        new_dict["updated_at"] = self.updated_at.isoformat(sep='T')
        return new_dict

