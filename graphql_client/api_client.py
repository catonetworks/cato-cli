# coding: utf-8

from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

# python 2 and python 3 compatibility library
import sys
sys.path.insert(0, 'vendor')
import certifi
import six
from six.moves.urllib.parse import urlencode

try:
	import urllib3
except ImportError:
	raise ImportError('GraphQL python client requires urllib3.')

logger = logging.getLogger(__name__)

class QUERYResponse(io.IOBase):

	def __init__(self, resp):
		self.urllib3_response = resp
		self.status = resp.status
		self.reason = resp.reason
		self.data = resp.data

	def getheaders(self):
		"""Returns a dictionary of the response headers."""
		return self.urllib3_response.getheaders()

	def getheader(self, name, default=None):
		"""Returns a given response header."""
		return self.urllib3_response.getheader(name, default)

class QUERYClientObject(object):

	def __init__(self, configuration, pools_size=4, maxsize=None):
		# urllib3.PoolManager will pass all kw parameters to connectionpool
		# https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
		# https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
		# maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
		# Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

		# cert_reqs
		if configuration.verify_ssl:
			cert_reqs = ssl.CERT_REQUIRED
		else:
			cert_reqs = ssl.CERT_NONE

		# ca_certs
		if configuration.ssl_ca_cert:
			ca_certs = configuration.ssl_ca_cert
		else:
			# if not set certificate file, use Mozilla's root certificates.
			ca_certs = certifi.where()

		addition_pool_args = {}
		if configuration.assert_hostname is not None:
			addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

		if maxsize is None:
			if configuration.connection_pool_maxsize is not None:
				maxsize = configuration.connection_pool_maxsize
			else:
				maxsize = 4

		# https pool manager
		if configuration.proxy:
			self.pool_manager = urllib3.ProxyManager(
				num_pools=pools_size,
				maxsize=maxsize,
				cert_reqs=cert_reqs,
				ca_certs=ca_certs,
				cert_file=configuration.cert_file,
				key_file=configuration.key_file,
				proxy_url=configuration.proxy,
				**addition_pool_args
			)
		else:
			self.pool_manager = urllib3.PoolManager(
				num_pools=pools_size,
				maxsize=maxsize,
				cert_reqs=cert_reqs,
				ca_certs=ca_certs,
				cert_file=configuration.cert_file,
				key_file=configuration.key_file,
				**addition_pool_args
			)

	def request(self, method, url, headers=None,
				body=None, _preload_content=True,
				_request_timeout=None):
		"""Perform requests.
		:param headers: http request headers
		:param body: request json body, for `application/json`
		:param _preload_content: if False, the urllib3.HTTPResponse object will
								 be returned without reading/decoding response
								 data. Default is True.
		:param _request_timeout: timeout setting for this request. If one
								 number provided, it will be total request
								 timeout. It can also be a pair (tuple) of
								 (connection, read) timeouts.
		"""
		method = method.upper()
		assert method in ['POST']
		headers = headers or {}

		timeout = None
		if _request_timeout:
			if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
				timeout = urllib3.Timeout(total=_request_timeout)
			elif (isinstance(_request_timeout, tuple) and
				  len(_request_timeout) == 2):
				timeout = urllib3.Timeout(
					connect=_request_timeout[0], read=_request_timeout[1])

		if 'Content-Type' not in headers:
			headers['Content-Type'] = 'application/json'

		try:
			if re.search('json', headers['Content-Type'], re.IGNORECASE):
				try:
					r = self.pool_manager.request( method=method, url=url,
						body=json.dumps(body),
						preload_content=_preload_content,
						timeout=timeout,
						headers=headers)
				except Exception as e:
					# remove the restriction for raw 
					print("ERROR: ",e)
					exit()
				
			else:
				# Cannot generate the request from given parameters
				msg = """Cannot prepare a request message for provided
						 arguments. Please check that your arguments match
						 declared content type."""
				raise ApiException(status=0, reason=msg)
			
		except urllib3.exceptions.SSLError as e:
			msg = "{0}\n{1}".format(type(e).__name__, str(e))
			raise ApiException(status=0, reason=msg)

		if _preload_content:
			r = QUERYResponse(r)

			# log response body
			logger.debug("response body: %s", r.data)

		if not 200 <= r.status <= 299:
			raise ApiException(http_resp=r)

		return r

	def POST(self, url, headers=None, body=None, _preload_content=True, _request_timeout=None):
		return self.request("POST", url, headers=headers,
							_preload_content=_preload_content,
							_request_timeout=_request_timeout,
							body=body)

class ApiException(Exception):

	def __init__(self, status=None, reason=None, http_resp=None):
		if http_resp:
			self.status = http_resp.status
			self.reason = http_resp.reason
			self.body = http_resp.data
			self.headers = http_resp.getheaders()
		else:
			self.status = status
			self.reason = reason
			self.body = None
			self.headers = None

	def __str__(self):
		"""Custom error messages for exception"""
		if self.body:
			# error_message += "HTTP response body:\n{}".format(self.body.decode('utf8'))
			return self.body.decode('utf8')
		else:
			error_message = "({0})\n"\
							"Reason: {1}\n".format(self.status, self.reason)
			if self.headers:
				error_message += "HTTP response headers: {0}\n".format(
					self.headers)

