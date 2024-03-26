import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
	__file_path = "file.json"
	__objects = {}

	def all(self):
		return FileStorage.__objects
	
	def new(self, obj):
		key = "{}.{}".format(obj.__class__.__name__, obj.id)
		self.__objects[key] = obj

	def save(self):
		serialized_objects = {}
		for key, value in self.__objects.items():
			serialized_objects[key] = value.to_dict()
		with open(self.__file_path, 'w') as file:
			json.dump(serialized_objects, file)


	def reload(self):
		"""Deserialize the json file to objects"""
		try:
			with open(self.__file_path, 'r') as file:
				data = json.load(file)
			for key, value in data.items():
				self.__objects[key] = eval(key.split('.')[0])(**value)
				
		except FileNotFoundError:
			pass
