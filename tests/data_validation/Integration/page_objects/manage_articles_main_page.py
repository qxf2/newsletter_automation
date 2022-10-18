"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .manage_articles_page import Managearticles_Object_Page
from .hamburger_object import Hamburger_Object

class Managearticles_Mainpage(Base_Page,Mail_Object, Hamburger_Object, Managearticles_Object_Page):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)
