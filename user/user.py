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

	print('FTPy - A Python implementation of FTP according to RFC959')
	password = getpass.getpass(prompt='Password: ')

	protocol_interpreter = UserPI(username, password, hostname, port)

	while True:
		user_input = input(User.prompt_msg)

		try:
			command, argument  = user_input.split()
			comm = 
		except:



		if command == 'quit':
			break

		protocol_interpreter.send(command)
		response = protocol_interpreter.receive()

		print(response)
