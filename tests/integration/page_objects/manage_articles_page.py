"""
This class models the newsletter main page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .search_object import Search_Object
from .table_object import Table_Object
from .hamburger_object import Hamburger_Object
from utils.Wrapit import Wrapit

class Managearticles_Page(Base_Page, Mail_Object, Hamburger_Object, Search_Object, Table_Object):
    "Page Object for the newsletter main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)

    #click manage article button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_managearticle_button(self):
     click_manage_article=self.click_element(self.manage_article)
     return click_manage_article
     