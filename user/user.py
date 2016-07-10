#!/usr/bin/python3
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

	protocol_interpreter.send("hello")
	response = protocol_interpreter.receive()

	print(response)




#	# validate user credentials
#	user_pi = UserPI(username, password, 8021)

#	while True:
#		command = input(User.prompt_msg)
#		command = command + '_command'
#
#		try:
#			result = getattr(user_pi, command)()
#		except AttributeError:
#			result = user_pi.ukn_command()
#
#		print(result)
#		if command == 'quit_command':
#			break
#
#	# close connection