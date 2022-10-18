"""
This class models the interviewscheduler_mainpage page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .edit_articles_object import Editarticles_Object
from .hamburger_object import Hamburger_Object

class Editarticles_Page(Base_Page,Mail_Object, Hamburger_Object,Editarticles_Object):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)
