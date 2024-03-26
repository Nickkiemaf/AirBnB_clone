#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class HBNBCCommand(cmd.Cmd):
	prompt = "(hbnb) "


	def do_create(self, arg):
		"""Class creates a new instance of BaseModel, save it, & print the id"""
		if not arg:
			print("** class name missing **")
			return
		
		try:
			new_instance = eval(arg)()
			new_instance.save()
			print(new_instance.id)
		
		except NameError:
			print("** class doesn't exist **")
		
	def do_show(self, arg):
		"""Print the string representation of an instance"""
		args = shlex.split(arg)
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			if class_name not in storage.classes():
				print("** class doesn't exist **")
				return
			if len(args) < 2:
				print("** instance id missing *")
				return
			obj_id = args[1]
			key = "{}.{}".format(class_name, obj_id)
			if key in storage.all():
				print(storage.all()[key])
			else:
				print("*** no instance found *")
		
		except Exception as e:
			print(e)

	def do_destroy(self, arg):
		"""This deletes an instance"""
		args = shlex.split(arg)
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			if class_name not in storage.classes():
				print("** class doesn't exist **")
				return
			if len(args) < 2:
				print("** instance id is missing **")
				return
			obj_id = args[1]
			key = "{}.{}".format(class_name, obj_id)
			if key in storage.all():
				del storage.all()[key]
				storage.save()
			else:
				print("** no instance found **")
		except Exception as e:
			print(e)

	def do_all(self, arg):
		"""This prints all instances"""
		args = shlex.split(arg)
		objects = storage.all()
		if not args:
			print([str(obj) for obj in objects.values()])
		else:
			try:
				class_name = args[0]
				if class_name not in storage.classes():
					print("** class doesn't exist **")
					return
				filtered_objects = [str(obj) for key, obj in objects.item() if key.split('.')[0] == class_name]
				print(filtered_objects)
			except Exception as e:
				print(e)

	def do_update(self, arg):
		"""This updates an instance"""
		args = shlex.split(arg)
		if not args:
			print("** class name missing **")
			return
		try:
			class_name = args[0]
			if class_name not in storage.classes():
				print("** class doesn't exist **")
				return
			if len(args) < 2:
				print("** instance id missing **")
				return
			obj_id = args[1]
			key = "{}.{}".format(class_name, obj_id)
			if key not in storage.all():
				print("** no instance found **")
				return
			if len(args) < 3:
				print("** attribute name missing **")
				return
			if len(args) < 4:
				print("** value missing **")
				return
			attr_name = args[2]
			attr_value = args[3]
			obj = storage.all()[key]
			try:
				sttr_value = eval(attr_value)
			except:
				pass
			setattr(obj, attr_name, attr_value)
			storage.save()
		except Exception as e:
			print(e)


	def do_quit(self, line):
		"""Quit command to exit the console"""
		return True
	
	def do_EOF(self, line):
		"""EOF command to exit the console"""

	def emptyline(self):
		"""Does nothing when an empty line is entered"""
		pass

if __name__ == '__main__':
	HBNBCCommand().cmdloop()
