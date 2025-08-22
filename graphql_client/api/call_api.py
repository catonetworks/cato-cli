# coding: utf-8

from __future__ import absolute_import
import re
import json

# python 2 and python 3 compatibility library
import sys
sys.path.insert(0, 'vendor')
import six
from graphql_client.api_client_types import ApiClient

class CallApi(object):
	def __init__(self, api_client=None):
		if api_client is None:
			api_client = ApiClient()
		self.api_client = api_client

	def call_api(self, body, args, **kwargs):  # noqa: E501
		(data) = self.call_api_with_http_info(body, args, **kwargs)  # noqa: E501
		return data
	
	def call_api_with_http_info(self, body, args, **kwargs):  # noqa: E501
		all_params = ['body', 'sync_type']  # noqa: E501
		all_params.append('async_req')
		if args.get("v")==True:
			all_params.append('_return_http_data_only')
			all_params.append('_preload_content')
			all_params.append('_request_timeout')

		params = locals()
		for key, val in six.iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method create_asset4" % key
				)
			params[key] = val
		del params['kwargs']

		if ('body' not in params or params['body'] is None):
			raise ValueError("Missing the required parameter `body` when calling `create_asset4`")  

		collection_formats = {}

		header_params = {}

		form_params = []
		local_var_files = {}

		body_params = None
		if 'body' in params:
			body_params = params['body']
			header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
			header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])
			# Only add x-api-key if not using custom headers
			using_custom_headers = hasattr(self.api_client.configuration, 'custom_headers') and self.api_client.configuration.custom_headers
			if not using_custom_headers and 'x-api-key' in self.api_client.configuration.api_key:
				header_params['x-api-key'] = self.api_client.configuration.api_key['x-api-key']
			header_params['User-Agent'] = "Cato-CLI-v"+self.api_client.configuration.version
		
		# Add custom headers from configuration with proper encoding handling
		if using_custom_headers:
			for key, value in self.api_client.configuration.custom_headers.items():
				# Ensure header values can be encoded as latin-1 (HTTP header encoding)
				try:
					# Try to encode as latin-1 first (HTTP standard)
					if isinstance(value, str):
						value.encode('latin-1')
					header_params[key] = value
				except UnicodeEncodeError:
					# If latin-1 encoding fails, encode as UTF-8 and then decode as latin-1
					# This handles Unicode characters by converting them to percent-encoded format
					if isinstance(value, str):
						try:
							# URL encode problematic Unicode characters
							import urllib.parse
							encoded_value = urllib.parse.quote(value, safe=':;=?@&')
							header_params[key] = encoded_value
						except Exception:
							# As a last resort, replace problematic characters
							header_params[key] = value.encode('ascii', 'replace').decode('ascii')

		if args.get("v")==True:
			print("Host: ",self.api_client.configuration.host)
			# Create a copy of header_params with masked API key for verbose output
			masked_headers = header_params.copy()
			if 'x-api-key' in masked_headers:
				masked_headers['x-api-key'] = '***MASKED***'
			print("Request Headers:",json.dumps(masked_headers,indent=4,sort_keys=True))
			print("Request Data:",json.dumps(body_params,indent=4,sort_keys=True),"\n\n")
			
		return self.api_client.call_api(
			header_params,
			body=body_params,
			files=local_var_files,
			response_type="NoSchema",  # noqa: E501 
			async_req=params.get('async_req'),
			_return_http_data_only=params.get('_return_http_data_only'),
			_preload_content=params.get('_preload_content', True),
			_request_timeout=params.get('_request_timeout'),
			collection_formats=collection_formats)
