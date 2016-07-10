#!/usr/bin/python

class Page:
	def __init__(self, header_length, index, data_length, page_type ):
		self.header_length = header_length
		self.index = index
		self.data_length = data_length
		self.page_type = page_type

