#!/usr/bin/python3

class UserPI:
	'''
		User Protocol Interpreter (port 20)
	'''

	def __init__(self, username, password, control_port, data_port=8020):
		self.username = username
		self.password = password
		self.control_port = control_port
		self.data_port = data_port

	# FTP Access control commands ----------------------------------------------
	def user_comand(self):
		'''
			User Name
		'''
		return 'user_comand'

	def pass_command(self):
		'''
			Password
		'''
		return 'pass_command'

	def acct_command(self):
		'''
			Account
		'''
		return 'acct_command'

	def cwd_command(self):
		'''
			Change Working Directory
		'''
		return 'cwd_command'

	def cdup_command(self):
		'''
			Change To Parent Directory
		'''
		return 'cdup_command'

	def smnt_command(self):
		'''
			Structure Mount
		'''
		return 'smnt_command'

	def rein_command(self):
		'''
			Reinitialize
		'''
		return 'rein_command'

	def quit_command(self):
		'''
			Logout
		'''
		return 'quit_command'


	# FTP Transfer parameter commands ------------------------------------------
	def port_command(self, data_port):
		'''
			Data Port
		'''
		return 'port_command'

	def pasv_command(self):
		'''
			Passive
		'''
		return 'pasv_command'

	def type_command(self, repr_type):
		'''
			Representation Type
		'''
		return 'type_command'

	def stru_command(self, file_structure):
		'''
			File Structure
		'''
		return 'stru_command'

	def mode_command(self, data_transfer_mode):
		'''
			Transfer Mode
		'''
		return 'mode_command'


	# FPT Service commands -----------------------------------------------------
	def retr_command(self, pathname):
		'''
			Retrieve
		'''
		return 'retr_command'

	def stor_command(self, pathname):
		'''
			Store
		'''
		return 'stor_command'

	def stou_command(self, pathname):
		'''
			Store Unique
		'''
		return 'stou_command'

	def appe_command(self, pathname):
		'''
			Append (with create)
		'''
		return 'appe_command'

	def allo_command(self, allocate_size):
		'''
			Allocate
		'''
		return 'allo_command'

	def rest_command(self):
		'''
			Restart
		'''
		return 'rest_command'

	def rnfr_command(self, old_pathname):
		'''
			Rename From
		'''
		return 'rnfr_command'

	def rnto_command(self, new_pathname):
		'''
			Rename To
		'''
		return 'rnto_command'

	def abor_command(self):
		'''
			Abort
		'''
		return 'abor_command'

	def dele_command(self, pathname):
		'''
			Delete
		'''
		return 'dele_command'

	def rmd_command(self, pathname):
		'''
			Remove Directory
		'''
		return 'rmd_command'

	def mkd_command(self, pathname):
		'''
			Make Directory
		'''
		return 'mkd_command'

	def pwd_command(self):
		'''
			Print Working Directory
		'''
		return 'pwd_command'

	def list_command(self, pathname=None):
		'''
			List
		'''
		return 'list_command'

	def nlst_command(self, pathname):
		'''
			Name List
		'''
		return 'nlst_command'

	def site_command(self):
		'''
			Site Parameters
		'''
		return 'site_command'

	def syst_command(self):
		'''
			System
		'''
		return 'syst_command'

	def help_command(self, command=None):
		'''
			Help
		'''
		return 'help_command'

	def noop_command(self):
		'''
			Noop (No-operation)
		'''
		return 'noop_command'

	# A command is only unkown to the server,
	# it has to give a response saying the command
	# is not known.
	def ukn_command(self):
		'''
			Unknow Command
		'''
		return 'ukn_command'

	








