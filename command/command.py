#!/usr/bin/python

class Command:
	def __init__(self, command, argument=''):
		self.command = command
		self.argument = argument

	def __str__(self):
		if self.argument:
			return self.command + '-' + self.argument
		return self.command
