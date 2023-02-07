"""
This class models the newsletter login page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object

class Login_Page(Base_Page, Mail_Object):
    "Page Object for the newsletter login page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = '/'
        self.open(url)
    
