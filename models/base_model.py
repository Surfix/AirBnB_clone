#!/usr/bin/python3
"""This is the Base Model For All Models."""

from datetime import datetime as dtime
from uuid import uuid4
import models


class BaseModel:
    """This Model Implement All common attribute for other model."""

    def __init__(self, id, created_at, updated_at):
        """Initialize the BaseModel."""
       self.id = str(uuid4())
       self.created_at = dtime.now()
       self.updated_at() = dtime.now()

    def __str__(self):
        """Return the string representation of BaseModel"""
        return f'[{self.__class__.__name__}] ({self.id}) (self.__dict__)'

    def save(self):
        """Update the BaseModel Data"""
        self.updated_at = dtime,now()

    def to_dict(self):
        """Return the dictionary representation of BaseModel."""
        attr = self.__dict__.copy()
        attr['__class__'] = self.__class__.__name__
        if not type(attr['created_at']) is str:
            attr['created_at'] = attr['created_at'].isoformat()
        if not type(attr['updated_at']) is str:
            attr['updated_at'] = attr['updated_at'].isoformat()
        return attr
