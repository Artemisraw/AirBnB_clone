#!/usr/bin/python3

"""This class defines all common attributes/method for classes"""
import uuid
import datetime
from  models import storage


class BaseModel:

    """
    """
    def __init__(self, *args, **kwags):
        self.id = str(uuid.uuid1())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__} "

    def save(self):
        updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        self.__dict__.update(
            {
                "__class__": self.__class__.__name__,
                "updated_at": self.updated_at.isoformat(),
                "id": self.id,
                "created_at": self.created_at.isoformat(),
            }
        )
        storage.new(self._dict__)
        return self.__dict__
