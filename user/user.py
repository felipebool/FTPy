#!/usr/bin/python3
from user_dtp import UserDTP
from user_pi import UserPI

class User():
	'''
		File Transfer Protocol User Interface
	'''
	prompt_msg = 'ftpy> '

	def __init__(self):
		pass

if __name__ == '__main__':
	interface = UserInterface()

	while True:
		command = input(UserInterface.prompt_msg)
		print(command)

		if command == 'quit':
			break

	# end connection