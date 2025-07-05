# coding: utf-8

from __future__ import absolute_import

import datetime
import json
import mimetypes
from multiprocessing.pool import ThreadPool
import os
import re
import tempfile

from graphql_client.configuration import Configuration
import graphql_client.models
from graphql_client import api_client

# python 2 and python 3 compatibility library
import sys
sys.path.insert(0, 'vendor')
import six

class ApiClient(object):
	PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
	NATIVE_TYPES_MAPPING = {
		'int': int,
		'long': int if six.PY3 else long,
		'float': float,
		'str': str,
		'bool': bool,
		'date': datetime.date,
		'datetime': datetime.datetime,
		'object': object,
	}

	def __init__(self, configuration=None, header_name=None, header_value=None,
				 cookie=None):
		if configuration is None:
			configuration = Configuration()
		self.configuration = configuration

		self.pool = ThreadPool()
		self.rest_client = api_client.QUERYClientObject(configuration)
		self.default_headers = {}
		if header_name is not None:
			self.default_headers[header_name] = header_value
		self.cookie = cookie
		self.user_agent = "Cato-CLI-v"+self.configuration.version

	def __del__(self):
		self.pool.close()
		self.pool.join()

	@property
	def user_agent(self):
		"""User agent for this API client"""
		return self.default_headers['User-Agent']

	@user_agent.setter
	def user_agent(self, value):
		self.default_headers['User-Agent'] = value

	def set_default_header(self, header_name, header_value):
		self.default_headers[header_name] = header_value

	def __call_api(
			self, header_params=None, body=None,
			files=None, response_type=None,
			_return_http_data_only=None, collection_formats=None,
			_preload_content=True, _request_timeout=None):

		config = self.configuration

		# header parameters
		header_params = header_params or {}
		header_params.update(self.default_headers)
		if self.cookie:
			header_params['Cookie'] = self.cookie
		if header_params:
			header_params = self.sanitize_for_serialization(header_params)
			header_params = dict(self.parameters_to_tuples(header_params,
														   collection_formats))

		# body
		if body:
			body = self.sanitize_for_serialization(body)

		# request url
		url = self.configuration.host

		# perform request and return response
		response_data = self.request(
			 url, headers=header_params, body=body,
			_preload_content=_preload_content,
			_request_timeout=_request_timeout)

		self.last_response = response_data

		return_data = response_data
		if _preload_content:
			# deserialize response data
			if response_type:
				return_data = self.deserialize(response_data, response_type)
			else:
				return_data = None

		# Temporarily commented out to allow custom error handling
		# if "errors" in return_data:
		#	print(json.dumps(return_data))
		#	exit(1)

		if _return_http_data_only:
			return (return_data)
		else:
			return (return_data, response_data.status,
					response_data.getheaders())

	def sanitize_for_serialization(self, obj):
		"""Builds a JSON POST object.
		If obj is None, return None.
		If obj is str, int, long, float, bool, return directly.
		If obj is datetime.datetime, datetime.date
			convert to string in iso8601 format.
		If obj is list, sanitize each element in the list.
		If obj is dict, return the dict.
		:param obj: The data to serialize.
		:return: The serialized form of data.
		"""
		if obj is None:
			return None
		elif isinstance(obj, self.PRIMITIVE_TYPES):
			return obj
		elif isinstance(obj, list):
			return [self.sanitize_for_serialization(sub_obj)
					for sub_obj in obj]
		elif isinstance(obj, tuple):
			return tuple(self.sanitize_for_serialization(sub_obj)
						 for sub_obj in obj)
		elif isinstance(obj, (datetime.datetime, datetime.date)):
			return obj.isoformat()

		if isinstance(obj, dict):
			obj_dict = obj
		else:
			obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
						for attr, _ in six.iteritems(obj.swagger_types)
						if getattr(obj, attr) is not None}

		return {key: self.sanitize_for_serialization(val)
				for key, val in six.iteritems(obj_dict)}

	def deserialize(self, response, response_type):
		# handle file downloading
		# save response body into a tmp file and return the instance
		if response_type == "file":
			return self.__deserialize_file(response)

		# fetch data from response object
		try:
			data = json.loads(response.data)
		except ValueError:
			data = response.data

		return self.__deserialize(data, response_type)

	def __deserialize(self, data, klass):
		if data is None:
			return None

		if type(klass) == str:
			if klass.startswith('list['):
				sub_kls = re.match(r'list\[(.*)\]', klass).group(1)
				return [self.__deserialize(sub_data, sub_kls)
						for sub_data in data]

			if klass.startswith('dict('):
				sub_kls = re.match(r'dict\(([^,]*), (.*)\)', klass).group(2)
				return {k: self.__deserialize(v, sub_kls)
						for k, v in six.iteritems(data)}

			# convert str to class
			if klass in self.NATIVE_TYPES_MAPPING:
				klass = self.NATIVE_TYPES_MAPPING[klass]
			else:
				klass = getattr(graphql_client.models, klass)

		if klass in self.PRIMITIVE_TYPES:
			return self.__deserialize_primitive(data, klass)
		elif klass == object:
			return self.__deserialize_object(data)
		elif klass == datetime.date:
			return self.__deserialize_date(data)
		elif klass == datetime.datetime:
			return self.__deserialize_datatime(data)
		else:
			return self.__deserialize_model(data, klass)

	def call_api(self, header_params=None, body=None, files=None,
				 response_type=None, async_req=None,
				 _return_http_data_only=None, collection_formats=None,
				 _preload_content=True, _request_timeout=None):

		if not async_req:
			return self.__call_api( header_params, body, files,
								   response_type, _return_http_data_only, collection_formats,
								   _preload_content, _request_timeout)
		else:
			thread = self.pool.apply_async(self.__call_api, ( header_params, 
										   body, files, response_type, 
										   _return_http_data_only,
										   collection_formats,
										   _preload_content, _request_timeout))
		return thread

	def request(self, url, headers=None, 
			 body=None, _preload_content=True,
			_request_timeout=None):

		return self.rest_client.POST(url, headers=headers,
									 _preload_content=_preload_content,
									 _request_timeout=_request_timeout,
									 body=body)

	def parameters_to_tuples(self, params, collection_formats):
		"""Get parameters as list of tuples, formatting collections.

		:param params: Parameters as dict or list of two-tuples
		:param dict collection_formats: Parameter collection formats
		:return: Parameters as list of tuples, collections formatted
		"""
		new_params = []
		if collection_formats is None:
			collection_formats = {}
		for k, v in six.iteritems(params) if isinstance(params, dict) else params:  # noqa: E501
			if k in collection_formats:
				collection_format = collection_formats[k]
				if collection_format == 'multi':
					new_params.extend((k, value) for value in v)
				else:
					if collection_format == 'ssv':
						delimiter = ' '
					elif collection_format == 'tsv':
						delimiter = '\t'
					elif collection_format == 'pipes':
						delimiter = '|'
					else:  # csv is the default
						delimiter = ','
					new_params.append(
						(k, delimiter.join(str(value) for value in v)))
			else:
				new_params.append((k, v))
		return new_params

	def select_header_accept(self, accepts):
		"""Returns `Accept` based on an array of accepts provided.

		:param accepts: List of headers.
		:return: Accept (e.g. application/json).
		"""
		if not accepts:
			return

		accepts = [x.lower() for x in accepts]

		if 'application/json' in accepts:
			return 'application/json'
		else:
			return ', '.join(accepts)

	def select_header_content_type(self, content_types):
		"""Returns `Content-Type` based on an array of content_types provided.

		:param content_types: List of content-types.
		:return: Content-Type (e.g. application/json).
		"""
		if not content_types:
			return 'application/json'

		content_types = [x.lower() for x in content_types]

		if 'application/json' in content_types or '*/*' in content_types:
			return 'application/json'
		else:
			return content_types[0]

	def __deserialize_file(self, response):
		"""Deserializes body to file

		Saves response body into a file in a temporary folder,
		using the filename from the `Content-Disposition` header if provided.

		:param response:  RESTResponse.
		:return: file path.
		"""
		fd, path = tempfile.mkstemp(dir=self.configuration.temp_folder_path)
		os.close(fd)
		os.remove(path)

		content_disposition = response.getheader("Content-Disposition")
		if content_disposition:
			filename = re.search(r'filename=[\'"]?([^\'"\s]+)[\'"]?',
								 content_disposition).group(1)
			path = os.path.join(os.path.dirname(path), filename)
			response_data = response.data
			with open(path, "wb") as f:
				if isinstance(response_data, str):
					# change str to bytes so we can write it
					response_data = response_data.encode('utf-8')
					f.write(response_data)
				else:
					f.write(response_data)
		return path

	def __deserialize_primitive(self, data, klass):
		"""Deserializes string to primitive type.

		:param data: str.
		:param klass: class literal.

		:return: int, long, float, str, bool.
		"""
		try:
			return klass(data)
		except UnicodeEncodeError:
			return six.text_type(data)
		except TypeError:
			return data

	def __deserialize_object(self, value):
		"""Return a original value.

		:return: object.
		"""
		return value

	def __deserialize_date(self, string):
		"""Deserializes string to date.

		:param string: str.
		:return: date.
		"""
		try:
			from dateutil.parser import parse
			return parse(string).date()
		except ImportError:
			return string
		except ValueError:
			raise apiclient.ApiException(
				status=0,
				reason="Failed to parse `{0}` as date object".format(string)
			)

	def __deserialize_datatime(self, string):
		"""Deserializes string to datetime.

		The string should be in iso8601 datetime format.

		:param string: str.
		:return: datetime.
		"""
		try:
			from dateutil.parser import parse
			return parse(string)
		except ImportError:
			return string
		except ValueError:
			raise apiclient.ApiException(
				status=0,
				reason=(
					"Failed to parse `{0}` as datetime object"
					.format(string)
				)
			)

	def __hasattr(self, object, name):
			return name in object.__class__.__dict__

	def __deserialize_model(self, data, klass):
		"""Deserializes list or dict to model.

		:param data: dict, list.
		:param klass: class literal.
		:return: model object.
		"""

		if not klass.swagger_types and not self.__hasattr(klass, 'get_real_child_model'):
			return data

		kwargs = {}
		if klass.swagger_types is not None:
			for attr, attr_type in six.iteritems(klass.swagger_types):
				if (data is not None and
						klass.attribute_map[attr] in data and
						isinstance(data, (list, dict))):
					value = data[klass.attribute_map[attr]]
					kwargs[attr] = self.__deserialize(value, attr_type)

		instance = klass(**kwargs)

		if (isinstance(instance, dict) and
				klass.swagger_types is not None and
				isinstance(data, dict)):
			for key, value in data.items():
				if key not in klass.swagger_types:
					instance[key] = value
		if self.__hasattr(instance, 'get_real_child_model'):
			klass_name = instance.get_real_child_model(data)
			if klass_name:
				instance = self.__deserialize(data, klass_name)
		return instance
