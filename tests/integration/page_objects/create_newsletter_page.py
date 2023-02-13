"""
This class models the newsletter create newsletter page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .form_object_create_newsletter import Form_Object_Create_Newsletter
from .hamburger_object import Hamburger_Object
import conf.create_newsletter_locator_conf as locators

class Createnewsletter_Page(Base_Page, Mail_Object, Hamburger_Object, Form_Object_Create_Newsletter):
    "Page Object for the create newsletter page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'create-newsletter'
        self.open(url)
