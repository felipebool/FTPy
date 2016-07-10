#!/usr/bin/python3

class UserPI():
	'''
		User Protocol Interpreter (port 20)
	'''

	def __init__(self, username, password, ctrl_port):
		self.username = username
		self.password = password
		self.ctrl_port = ctrl_port

	# FTP Access control commands ----------------------------------------------
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


	# FTP Transfer parameter commands ------------------------------------------
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


	# FPT Service commands -----------------------------------------------------
	def retr_command(self, pathname):
		'''
			Retrieve
		'''
		pass

	def stor_command(self, pathname):
		'''
			Store
		'''
		pass

	def stou_command(self, pathname):
		'''
			Store Unique
		'''
		pass

	def appe_command(self, pathname):
		'''
			Append (with create)
		'''
		pass

	def allo_command(self, allocate_size):
		'''
			Allocate
		'''
		pass

	def rest_command(self):
		'''
			Restart
		'''
		pass

	def rnfr_command(self, old_pathname):
		'''
			Rename From
		'''
		pass

	def rnto_command(self, new_pathname):
		'''
			Rename To
		'''
		pass

	def abor_command(self):
		'''
			Abort
		'''
		pass

	def dele_command(self, pathname):
		'''
			Delete
		'''
		pass

	def rmd_command(self, pathname):
		'''
			Remove Directory
		'''
		pass

	def mkd_command(self, pathname):
		'''
			Make Directory
		'''
		pass

	def pwd_command(self):
		'''
			Print Working Directory
		'''
		pass

	def list_command(self, pathname=None):
		'''
			List
		'''
		pass

	def nlst_command(self, pathname):
		'''
			Name List
		'''
		pass

	def site_command(self):
		'''
			Site Parameters
		'''
		pass

	def syst_command(self):
		'''
			System
		'''
		pass

	def help_command(self, command=None):
		'''
			Help
		'''
		pass

	def noop_command(self):
		'''
			Noop (No-operation)
		'''
		pass

	








