#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
	"""This user class inherit from BaseModel"""

	def __init__ (self, *args, **kwargs):
		"""a constructor for the class User"""
		super().__init__(*args, **kwargs)
		self.email = ""
		self.password = ""
		self.first_name = ""
		self.last_name = ""
