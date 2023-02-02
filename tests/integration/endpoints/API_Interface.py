"""
A composed interface for all the API objects
Use the API_Player to talk to this class
"""
import requests
from .Base_API import Base_API
from .Article_API_Endpoints import Article_API_Endpoints 
from .Delete_Article_Endpoints import Delete_Article_Endpoints
from conf import base_url_conf as conf

class API_Interface(Base_API,Article_API_Endpoints,Delete_Article_Endpoints):
	"A composed interface for the API objects"

	def __init__(self, url, session_flag=False):
		"Constructor"
		# make base_url available to all API endpoints
		self.request_obj = requests
		if session_flag:
			self.create_session()
		self.base_url = url

	def create_session(self):
		"Create a session object"
		self.request_obj = requests.Session()

		return self.request_obj
