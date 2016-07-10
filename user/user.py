#!/usr/bin/python

import sys
import getpass

from user_dtp import UserDTP
from user_pi import UserPI

class User:
	'''
		File Transfer Protocol User Interface
	'''
	prompt_msg = 'ftpy> '

	def __init__(self):
		pass

if __name__ == '__main__':
	# username@hostname:portnumber
	credentials, port = sys.argv[1].split(':')
	username, hostname = credentials.split('@')

	# print(username)
	# print(hostname)
	# print(port)

	# exit()
	print('FTPy - A Python implementation of FTP according to RFC959')
	password = getpass.getpass(prompt='Password: ')

	protocol_interpreter = UserPI(username, password, hostname, port)

	# protocol_interpreter.send("hello")
	# response = protocol_interpreter.receive()

	# validate user credentials

	while True:
		command = input(User.prompt_msg)

		if command == 'quit':
			break

		response = protocol_interpreter.send(command)
		print(response)

	# close connection