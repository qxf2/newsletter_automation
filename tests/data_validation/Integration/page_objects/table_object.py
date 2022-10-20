from re import search
import conf.manage_articles_locator_conf as locators
from utils.Wrapit import Wrapit

class Table_Object:
    # get the delete locator
    delete =locators.delete
    
    # click delete button 
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_delete_button(self):
     delete_button=self.click_element(self.delete)
     return delete_button 
