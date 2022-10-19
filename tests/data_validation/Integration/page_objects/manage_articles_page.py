"""
This class models the newsletter_page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .manage_articles_object import Managearticles_Object
from .hamburger_object import Hamburger_Object

class Managearticles_Page(Base_Page,Mail_Object, Hamburger_Object, Managearticles_Object):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)
