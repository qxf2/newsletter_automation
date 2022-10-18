"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .add_articles_object import Addarticles_Object
from .hamburger_object import Hamburger_Object

class Addarticles_Page(Base_Page,Mail_Object, Hamburger_Object, Addarticles_Object):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'articles'
        self.open(url)
