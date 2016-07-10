#!/usr/bin/python3
from server_pi import ServerPI
from server_dtp import ServerDTP

class Server:
	'''
		File Transfer Protocol Server
	'''
	def __init__(self, control_port=65021, data_port=65020):
		self.control_port = control_port
		self.data_port = data_port

	def listen(self, port):
		print(port)

if __name__ == "__main__":
	protocol_interperter = ServerPI()

