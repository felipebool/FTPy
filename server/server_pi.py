#!/usr/bin/python3

import serversocket

class ServerPI(socketserver.BaseRequestHandler):
	'''
		Server Protocol Interpreter (port 20)
	'''
	def __init__(self, control_port=65021):
		self.control_port = control_port
		self.socket = self.listen()

	def handle(self):
		self.data = self.request(1024)
		print(self.data)
