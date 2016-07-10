#!/usr/bin/python

import socket

class UserPI:
	'''
		User Protocol Interpreter
	'''
	def __init__(self, username, password, hostname, control_port):
		self.username = username
		self.password = password
		self.hostname = hostname
		self.control_port = control_port
		self.socket = self.create_socket()

	def create_socket(self):
		return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.socket.connect((self.hostname, int(self.control_port)))

	def send(self, data):
		'''send
			Until this point, messages to be sent must be less than 1024
		'''
		self.socket.sendall(bytes(data + "\n", "utf-8"))
		
	def receive(self):
		return str(self.socket.recv(1024), "utf-8")

	def close(self):
		self.socket.close()