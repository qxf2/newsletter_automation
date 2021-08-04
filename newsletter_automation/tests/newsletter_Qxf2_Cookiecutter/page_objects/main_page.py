"""
This class models the Qxf2.com header as a Page Object.
The header consists of the Qxf2 logo, Qxf2 tag-line and the hamburger menu
Since the hanburger menu is complex, we will model it as a separate object  
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Main_Page(Base_Page):
    "Page Object for the Main_Page class"

    #locators

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
    
    @Wrapit._exceptionHandler
    def get_URL(self):
        "Check current URL"
        return self.get_current_url()

    

    
