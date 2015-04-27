from .config import *
from urllib.parse import urlencode, quote_plus 
# from urllib.request import urlopen
import requests
import json
class IltOAuthClient:
	"""
	TODO: readme
	"""
	_client_key = CLIENT_KEY
	_client_secret = CLIENT_SECRET
	_host_url = HOST_URL
	_redirect_url = REDIRECT_URL
	_auth_srv_url = _host_url + '/auth_server'
	_res_srv_url = _host_url + '/resource_server'
	_res_owner_url = _host_url + '/resource_owner'
	_scope = SCOPE
	_query_str = {
		'client_key' : _client_key,
		'redirect_uri' : quote_plus(_redirect_url),
		'scope' : _scope,
	}
	ilt_redirect_url = '{0}?{1}'.format(
			_auth_srv_url,
			urlencode(_query_str)
			)
	def __init__(self, request):
		pass
	def __del__(self):
		pass

	def getData(token):
		res_url_query_str = {
			'token' : token,
			'client_key' : IltOAuthClient._client_key,
			'client_secret' : IltOAuthClient._client_secret,
		}
		res_url = '{0}?{1}'.format(
			IltOAuthClient._res_srv_url,
			urlencode(res_url_query_str)
			)
		print (res_url)
		## 2015/04/27 edit by lego
		## I don't know how to use urllib to get response by HTTPS protocol
		# page = urlopen(res_url).read()
		
		page = requests.get(res_url)
		data = json.loads(page.text)
		return data
