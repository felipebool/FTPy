#!/usr/bin/python3
import server_pi
import server_dtp

class Server:
	'''
		File Transfer Protocol Server
	'''
	def __init__(self, control_port, data_port=8020):
		self.control_port = control_port
		self.data_port = data_port

	def listen(self, port):
		print(port)

if __name__ == "__main__":
	server = Server(8021)

	print(server.control_port)	
	print(server.data_port)

	