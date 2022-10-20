"""
This class models the newsletter_page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .search_object import Search_Object
from .table_object import Table_Object
from .hamburger_object import Hamburger_Object
from utils.Wrapit import Wrapit

class Managearticles_Page(Base_Page,Mail_Object, Hamburger_Object, Search_Object,Table_Object):
    "Page Object for the weather shopper main page"

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'manage-articles'
        self.open(url)

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def delete_article(self,search):
        "Submit the article"
        result_flag = self.click_hamburger_button()
        result_flag = self.click_managearticle_button()
        result_flag = self.set_search(search)  
        result_flag = self.click_delete_button()
        