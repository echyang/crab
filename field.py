#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functions import get_params 
from field_factory import *


class CrabField():

	field = None	
	ValCount = 'Only'
	ValFrom  = 'Val'
	attrList = ['content', 'image', 'link']

	def __init__(self, soup,  params):
		if params.has_key('multi') and params['multi']:
			self.ValCount = 'Multi'
		if params.has_key('attr') and  params['attr'] and params['attr'] in self.attrList:
			self.ValFrom = params['attr'].capitalize()
		else:
			self.ValFrom = 'Attr'
				
		#print self.ValCount+self.ValFrom
		self.field = eval(self.ValCount+self.ValFrom+'Field')(soup, params) 
		self.field.get_field()
	
	def get_data(self):
		return self.field.get_data()



if __name__ == "__main__":
	from functions import get_soup 
	url = 'http://www.jidujiao.com/shuku/files/article/html/0/399/9876.html'

	field_params =  {'name':'content', 'select':'div#content', 'attr':'Content', 'regex':'', 'number':0}	
	field_params =  {'name':'title', 'select':'div#title', 'attr':'val', 'regex':'', 'number':0}	
	field_params =  {'name':'title', 'select':'div#title', 'attr':'id', 'regex':'', 'number':0}	
	field_params =  {'name':'title', 'select':'div#linkleft a', 'attr':'link', 'regex':'', 'number':3}	
	field_params =  {'name':'title', 'select':'div#linkleft a', 'multi':True, 'attr':'link', 'regex':'', 'number':3}	

	url = 'http://www.bzcm.net/news/node_467_2.htm'
	field_params =  {'name':'title', 'select':'div#displaypagenum a', 'multi':True, 'attr':'href', 'regex':'', 'number':3}	

	soup = get_soup(url) 
	field_cur = CrabField(soup, field_params)
	print field_cur.get_data()


	
