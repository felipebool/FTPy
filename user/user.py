#!/usr/bin/python3
import sys
import getpass

from user_dtp import UserDTP
from user_pi import UserPI

# It was used 'User' rather than 'Client' because, strangely, the word
# Client is never mentioned in the entire RFC959.

class User:
	'''
		File Transfer Protocol User Interface
	'''
	prompt_msg = 'ftpy> '

	def __init__(self):
		pass

if __name__ == '__main__':
	# usage: ftpy <username>@<hostname>

	username, hostname = sys.argv[1].split('@')

	print('FTPy - A Python implementation of FTP according to RFC959')
	password = getpass.getpass(prompt='Password: ')

	# validate user credentials
	user_pi = UserPI(username, password, 8021, 8020)

	while True:
		command = input(User.prompt_msg)
		command = command + '_command'

		try:
			result = getattr(user_pi, command)()
		except AttributeError:
			result = user_pi.ukn_command()

		print(result)
		if command == 'quit_command':
			break

	# close connection