import json

from crud_module.common_utils import DateEncoder


class Loginlog(object):

	def __init__(self):
		self.__id = None
		self.__user_id = None
		self.__user_name = None
		self.__login_ip = None
		self.__login_ip_city_name = None
		self.__login_time = None
		self.__referer = None
		self.__device_type = None
		self.__browser_type = None
		self.__browser_version = None
		self.__login_url = None
		self.__user_agent = None
		self.__os = None
		self.__user_os = None
		self.__net_type = None
		pass

	def get_id(self):
		return self.__id

	def set_id(self, id):
		self.__id = id

	def get_user_id(self):
		return self.__user_id

	def set_user_id(self, user_id):
		self.__user_id = user_id

	def get_user_name(self):
		return self.__user_name

	def set_user_name(self, user_name):
		self.__user_name = user_name

	def get_login_ip(self):
		return self.__login_ip

	def set_login_ip(self, login_ip):
		self.__login_ip = login_ip

	def get_login_ip_city_name(self):
		return self.__login_ip_city_name

	def set_login_ip_city_name(self, login_ip_city_name):
		self.__login_ip_city_name = login_ip_city_name

	def get_login_time(self):
		return self.__login_time

	def set_login_time(self, login_time):
		self.__login_time = login_time

	def get_referer(self):
		return self.__referer

	def set_referer(self, referer):
		self.__referer = referer

	def get_device_type(self):
		return self.__device_type

	def set_device_type(self, device_type):
		self.__device_type = device_type

	def get_browser_type(self):
		return self.__browser_type

	def set_browser_type(self, browser_type):
		self.__browser_type = browser_type

	def get_browser_version(self):
		return self.__browser_version

	def set_browser_version(self, browser_version):
		self.__browser_version = browser_version

	def get_login_url(self):
		return self.__login_url

	def set_login_url(self, login_url):
		self.__login_url = login_url

	def get_user_agent(self):
		return self.__user_agent

	def set_user_agent(self, user_agent):
		self.__user_agent = user_agent

	def get_os(self):
		return self.__os

	def set_os(self, os):
		self.__os = os

	def get_user_os(self):
		return self.__user_os

	def set_user_os(self, user_os):
		self.__user_os = user_os

	def get_net_type(self):
		return self.__net_type

	def set_net_type(self, net_type):
		self.__net_type = net_type


	def __str__(self):
		loginlogDict = {'id':self.__id,'user_id':self.__user_id,'user_name':self.__user_name,'login_ip':self.__login_ip,'login_ip_city_name':self.__login_ip_city_name,'login_time':self.__login_time,'referer':self.__referer,'device_type':self.__device_type,'browser_type':self.__browser_type,'browser_version':self.__browser_version,'login_url':self.__login_url,'user_agent':self.__user_agent,'os':self.__os,'user_os':self.__user_os,'net_type':self.__net_type}
		return json.dumps(loginlogDict , cls=DateEncoder)
