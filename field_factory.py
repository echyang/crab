#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import get_params 

class FieldFactory():
	""" 数据字段获取
		
	"""
	
	_soup = None
	_data = None
	_params = None
	_params_template = {'name':'', 'select':'', 'multi':False, 'attr':'val', 'number':0 }

	def __init__(self, soup, params):
		self._soup = soup
		self._params = get_params(self._params_template, params)
		if not self._params['multi']:
			self._params['number'] = int(self._params['number'])-1>0 and int(self._params['number'])-1 or 0

	
	def get_field(self):
		pass

	
	def get_data(self):
		return {'name':self._params['name'], 'data':self._data}	



class MultiValField(FieldFactory):
	def get_field(self):
		self._data = [str(x) for x in self._soup.select(self._params['select'])] 


class MultiAttrField(FieldFactory):
	def get_field(self):
		self._data = [str(x[self._params['attr']]) for x in self._soup.select(self._params['select'])] 


class MultiImageField(FieldFactory):
	def get_field(self):
		pass
		

class MultiLinkField(FieldFactory):
	def get_field(self):
		self._data = [{'href':x['href'], 'text':x.get_text().strip()} for x in self._soup.select(self._params['select'])]


class MultiFileField(FieldFactory):
	def get_field(self):
		pass
		



class OnlyValField(FieldFactory):
	def get_field(self):
		self._data = self._soup.select(self._params['select'])[self._params['number']].get_text().strip()


class OnlyAttrField(FieldFactory):

	def get_field(self):
		self._data = self._soup.select(self._params['select'])[self._params['number']][self._params['attr']]


class OnlyContentField(FieldFactory):
	def get_field(self):
		self._data = "".join([unicode(x) for x in self._soup.select(self._params['select'])[self._params['number']].contents])


class OnlyImageField(FieldFactory):
	def get_field(self):
		pass
		

class OnlyLinkField(FieldFactory):
	def get_field(self):
		self._data = {'href':self._soup.select(self._params['select'])[self._params['number']]['href'], 'text':self._soup.select(self._params['select'])[self._params['number']].get_text().strip()}


class OnlyFileField(FieldFactory):
	def get_field(self):
		pass
		
