#!/usr/bin/python3
"""
"""
import os.path
import json
from datetime import datetime

class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in objects the obj in the format classname.id

        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
         serealise the object into a json file

        """
        with open( FileStorage.__file_path, 'w', encoding="utf-8") as file:
            data = {k: v.todict() for k,v in FileStorage.__objects.items()}
            json.dump(data, f)

    def classes(self):
        """
        Returns the dictionary of valid classes and theire refernces

        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = { "BaseModel": BaseModel,
                    "User" : User,
                    "State" : State,
                    "City" : City,
                    "Amenity" : Amenity,
                    "Place" : Place,
                    "Review" : Review}
        return classes
    
    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open( FileStorage.__file_path, 'r', encoding="utf-8") as file:
            result_dict = json.load(file)
            result_dict = {k: self.classes()[v["__class__"]](**v)
                           for k, v in result_dict.items()}

            FileStorage.__objects = result_dict

    def attributes(self):
        """
        Returns the valid attributes and their types 

        """

        attributes = {
                "BaseModel":{ "id": str,
                              "created_at": datetime.datetime,
                              "Updated_at": datetime.datetime},
                

                "User" : { "email": str,
                           "password": str,
                           "first_name": str,
                           "last_name": str},
                

                "State" : { "name" : str},

                
                "City" : {"state_id" : str,
                          "name" : str},

                
                "Amenity": { "name": str},

                
                "Place" : { "city_id" : str,
                            "user_id" : str,
                            "name" : str,
                            "description" : str,
                            "number_rooms" : str,
                            "number_bathrooms" : str,
                            "max_guest" : int,
                            "price_by_night" : int,
                            "latitude" : float,
                            "longitude" : float,
                            "amenity_ids": list},
                

                "Review" : { "place_id" : str,
                             "user_id" : str,
                             "text" : str}
                }
        return attributes
