#!/usr/bin/env python
# -*- coding: utf-8 -*-

from field import CrabField
from functions import get_params, get_soup, get_realurl 

class CrabSiblings():
	
	_pages = [] 
	_opened = []
	_params_template = {'name':'siblings', 'select':'', 'multi':True, 'attr':'href'}
	
	def __init__(self, soup, url,  params):
		self._params = get_params(self._params_template, params)
		print self._params
		field = CrabField(soup, self._params) 
		data = field.get_data()
		print data
		self._opened.append(url)
		self._pages.extend([get_realurl(url, x) for x in data['data']])
		print self._pages
		self.find()


	def find(self): 
		for cur_page in self._pages:
			print cur_page
			if cur_page not in self._opened:
				soup = get_soup(cur_page)	
				field = CrabField(soup, self._params) 
				data = field.get_data()
				for x in data['data']:
					new_page = get_realurl(cur_page, x)
					if not(new_page in self._pages or new_page in self._opened):
						if new_page not in self._opened:
							self._pages.append(new_page)
				self._opened.append(cur_page)
			
	def get_data(self):
		return self._opened
		
		
if __name__ == "__main__":
	from functions import get_soup 
	'''
	url = 'https://www.douban.com/group/flask/discussion?start=0'
	soup = get_soup(url) 
	params =  {'select':'div.paginator a'}	
	'''
	url = 'http://www.bzcm.net/news/node_467.htm'
	soup = get_soup(url) 
	params =  {'select':'div#displaypagenum a'}	

	siblings = CrabSiblings(soup, url, params)
	print siblings.get_data()



