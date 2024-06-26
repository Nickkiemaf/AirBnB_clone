#!/usr/bin/python3

import uuid
from datetime import datetime
import models

class BaseModel:
	def __init__(self, **kwargs):
		if kwargs:
			for key, value in kwargs.items():
				if key == 'created_at' or key == 'updated_at':
					setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
				elif key != '__class__':
					setattr(self, key, value)
		else:	
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			models.storage.new(self)

	def __str__(self):
		return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)
	
	
	def save(self):
		self.updated_at = datetime.now()
		models.storage.save()

	def to_dict(self):
		obj_dict = self.__dict__.copy()
		obj_dict['__class__'] = self.__class__.__name__
		obj_dict['created_at'] = self.created_at.isoformat()
		obj_dict['updated_at'] = self.updated_at.isoformat()
		return obj_dict


