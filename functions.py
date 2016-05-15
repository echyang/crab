# -*- coding:utf-8 -*-
import copy
import types
from bs4 import BeautifulSoup
import requests
import urlparse

def get_params(params_template, cur_params):
	data = copy.copy(params_template)
	if type(cur_params) is dict:
		data.update(cur_params)
	return data

def get_page(url):
	response = None
	try:
		s = requests.Session()
		response = s.get(url)
		if response.encoding == 'ISO-8859-1':
			encodings = requests.utils.get_encodings_from_content(response.content)
			if encodings:
				response.encoding = encodings[0]
			else:
				response.encoding = response.apparent_encoding
	except requests.RequestException as e:
		print e
	return response.content.decode(response.encoding, 'replace')


def get_soup(url):	
	return  BeautifulSoup(get_page(url), 'lxml')


def get_realurl(cur_url='', rel_url=''):
	url = ''	
	o =  urlparse.urlparse(url)
	if not o.netloc:
		cur_url = url_encode(cur_url)
		if cur_url and rel_url:
			url = urlparse.urljoin(cur_url, rel_url)
			url = reduce(lambda r,x:r.replace(x[0], x[1]), [('/../', '/')], url)	
	else:
		url = rel_url
	url = url.replace("../", '')
	url = url.replace("./", '')
	return url


def get_realurl(cur_url='', rel_url=''):
	url = ''	
	o =  urlparse.urlparse(url)
	if not o.netloc:
		cur_url = url_encode(cur_url)
		if cur_url and rel_url:
			url = urlparse.urljoin(cur_url, rel_url)
			url = reduce(lambda r,x:r.replace(x[0], x[1]), [('/../', '/')], url)	
	else:
		url = rel_url
	url = url.replace("../", '')
	url = url.replace("./", '')
	return url


def url_encode(url):
	o =  urlparse.urlparse(url)
	params = {}
	query = ''
	if o.query:
		for query_i in o.query.split('&'):
			params[query_i.split('=')[0]] =  urllib.quote(query_i.split('=')[1].decode('utf-8').encode('gb2312'))
		query = "&".join([k+'='+params[k] for k in params])
	return urlparse.urlunparse((o.scheme, o.netloc, o.path, '', query, ''))

def url_decode(url):
	o =  urlparse.urlparse(url)
	params = {}
	query = ''
	if o.query:
		for query_i in o.query.split('&'):
			params[query_i.split('=')[0]] =  urllib.unquote(query_i.split('=')[1]).decode('gb2312').encode('utf-8')
		query = "&".join([k+'='+params[k] for k in params])
	return urlparse.urlunparse((o.scheme, o.netloc, o.path, '', query, ''))


	
if __name__ == "__main__":
	url = 'http://www.jidujiao.com/shuku/files/article/html/0/399/9876.html'
	soup = get_soup(url) 
	print "".join([unicode(x) for x in soup.select('div#content')[0].contents])
