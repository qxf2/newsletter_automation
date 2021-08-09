"""
This class models the Qxf2.com header as a Page Object.
The header consists of the Qxf2 logo, Qxf2 tag-line and the hamburger menu
Since the hanburger menu is complex, we will model it as a separate object  
"""
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Home_Page(Base_Page):
    "Page Object for the Home_Page class"

    #locators
    header_text = locators.header_text

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
    
    @Wrapit._exceptionHandler
    def get_URL(self):
        "Check current URL"
        return self.get_current_url()
    
    @Wrapit._exceptionHandler
    def get_page_header(self):
        "Get header of the page"
        page_header = self.get_text(self.header_text).decode('utf-8') 
        print("The page header is ", page_header)

        return page_header

    @Wrapit._exceptionHandler
    def check_page_header(self):
        "Check header of the page"
        result_flag = False
        actual_header = self.get_page_header()
        expected_header = "Qxf2 Newsletter App"

        if actual_header == expected_header:
            result_flag = True
        return result_flag

    

    
