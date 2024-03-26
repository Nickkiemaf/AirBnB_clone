#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor for Amenity class"""
        super().__init__(*args, **kwargs)
        self.name = ""
