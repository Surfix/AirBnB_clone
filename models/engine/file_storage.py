#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    "Serializes instances to a JSON and deserializes JSON file to instances"
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)

            for key, obj_dic in new_obj_dict.items():
                if key not in self.__objects:
                    name = obj_dic['__class__']
                    base = eval(f"{name}(**obj_dic)")
                    self.new(base)
        except FileNotFoundError:
            pass

