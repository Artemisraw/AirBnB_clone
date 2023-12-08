#!/usr/bin/python3
"""
"""
import os.path
import json

class FileStorage:
    """
    """

    def __init__(self, *args, **kwargs):
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        return self.__objects

    def new(self, obj):
        print(obj)
        """key = obj["__class__"] + "." + obj["id"]
        self.__objects.update({key : obj})"""
        print("this is the self.__objects")
        print(self.__objects)

    def save(self):
        with open( self.__file_path, 'a', encoding="utf-8") as file:
            data = json.dumps(self.__objects)
            print(data)
            """file.write(data)"""
    
    def reload(self):
        if os.path.isfile("~/AirBnB_clone/"+self.__file_path) is True:
            with open( self.__file_path, 'r' , encoding="utf-8") as file:
                """data = file.read()"""
                data = json.loads(file.read())
                print(data)

        else:
            pass


