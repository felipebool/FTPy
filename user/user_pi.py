#!/usr/bin/python3

class UserPI():
	'''
		User Protocol Interpreter (port 20)
	'''

	# FTP Access control commands
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def user_comand(self):
		'''
			User Name
		'''
		pass

	def pass_command(self):
		'''
			Password
		'''
		pass

	def acct_command(self):
		'''
			Account
		'''
		pass

	def cwd_command(self):
		'''
			Change Working Directory
		'''
		pass

	def cdup_command(self):
		'''
			Change To Parent Directory
		'''
		pass

	def smnt_command(self):
		'''
			Structure Mount
		'''
		pass

	def rein_command(self):
		'''
			Reinitialize
		'''
		pass

	def quit_command(self):
		'''
			Logout
		'''
		pass

	# FTP Transfer parameter commands
	def port_command(self, data_port):
		'''
			Data Port
		'''
		pass

	def pasv_command(self):
		'''
			Passive
		'''
		pass

	def type_command(self, repr_type):
		'''
			Representation Type
		'''
		pass

	def stru_command(self, file_structure):
		'''
			File Structure
		'''
		pass

	def mode_command(self, data_transfer_mode):
		'''
			Transfer Mode
		'''
		pass

	# FPT Service commands
	

	