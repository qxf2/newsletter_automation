"""
This class models the newsletter main page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .form_object import Form_Object
from .hamburger_object import Hamburger_Object

class Addarticles_Page(Base_Page, Mail_Object, Hamburger_Object, Form_Object):
    "Page Object for the newsletter main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'articles'
        self.open(url)
