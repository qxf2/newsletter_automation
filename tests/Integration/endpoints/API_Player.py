"""
API_Player class does the following:
a) serves as an interface between the test and API_Interface
b) contains several useful wrappers around commonly used combination of actions
c) maintains the test context/state
"""
from base64 import b64encode
from .API_Interface import API_Interface
from utils.results import Results
import urllib.parse
import logging
from conf import api_example_conf as conf
from utils import interactive_mode
import pytest
from _pytest import python
from _pytest import config
import os



class API_Player(Results):
    "The class that maintains the test context/state"

    def __init__(self, url, log_file_path=None, session_flag=False):
        "Constructor"

        super(API_Player, self).__init__(
            level=logging.DEBUG, log_file_path=log_file_path)
        self.api_obj = API_Interface(url=url, session_flag=session_flag)

    def set_url(self,url):

        self.url=url
        return self.url


    def set_header_details(self, auth_details=None):
        "make header details"
        if auth_details != '' and auth_details is not None:
            headers = {'Authorization': "Basic %s"%(auth_details)}
        else:
            headers = {'content-type': 'application/json'}

        return headers


    def add_article(self, article_details, headers=None):
        "adds a new article"
        data = conf.article_details
        json_response = self.api_obj.add_article(data=data,
                headers=headers)
        print(f"JSON response:{json_response['response']}")
        result_flag = True if json_response['response']['successful'] == True else False

        return result_flag


    


    


    

   

    


    


    


    
    