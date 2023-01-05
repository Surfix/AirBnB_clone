#!/usr/bin/python3

import uuid
import datetime

""" Parent class to all classes of the AirBnB clone project """

class BaseModel():
    """Base Model class that other classes inherit from"""
    def __init__(self):
        """initializes object of the BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return the string representation of the BaseModel"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the Basemodel object's updated_at attribute"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return the dictionary representation of the BaseModel object"""
        ins_dict = self.__dict__
        ins_dict["__class__"] = self.__class__.__name__
        if type(ins_dict["created_at"]) is not str:
            ins_dict["created_at"] = ins_dict["created_at"].isoformat()
        if type(ins_dict["updated_at"]) is not str:
            ins_dict["updated_at"] = ins_dict["updated_at"].isoformat()
        return ins_dict
