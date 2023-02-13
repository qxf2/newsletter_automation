"""
This class models the add article page.

"""
from .Base_Page import Base_Page
from .form_object import Form_Object
from .hamburger_object import Hamburger_Object

class Addarticles_Page(Base_Page, Hamburger_Object, Form_Object):
    "Page Object for the newsletter main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'articles'
        self.open(url)
