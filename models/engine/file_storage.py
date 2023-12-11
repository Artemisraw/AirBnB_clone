#!/usr/bin/python3
"""
"""
import os.path
import json
from datetime import datetime

class FileStorage:
    """
    """

    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj, *argv):
        for arg in argv:
            key = arg + "." + obj["id"]
        self.__objects.update({key : obj})

    def save(self):
        with open( self.__file_path, 'a', encoding="utf-8") as file:
            data = json.dumps(self.__objects)
            file.write(data)
            file.write("\n")
    
    def reload(self):
        if  os.path.exists(self.__file_path):
            with open( self.__file_path, 'r' , encoding="utf-8") as file:
                for line in file:
                    data = json.loads(line)
            print(data) 
        else:
            pass
