#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():
    "Serializes instances to a JSON and deserializes JSON file to instances"
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        """ returns the dictionary for all objects"""
        return self.__objects

    def new(self, obj):
        """adds obj to __object"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Convert json file to dictionary"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)

            for key, obj_dic in new_obj_dict.items():
                if key not in self.__objects:
                    name = obj_dic['__class__']
                    base = eval(f"{name}(**obj)")
                    self.new(base)
        except FileNotFoundError:
            pass

