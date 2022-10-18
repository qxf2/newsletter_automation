from re import search
import conf.manage_articles_locator_conf as locators
from utils.Wrapit import Wrapit

class Managearticles_Object:
    # get the manage articles locator
    manage_article=locators.manage_article
    # get the search locator
    search =locators.search
    # get the delete locator
    delete =locators.delete
    
    # click manage article button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_managearticle_button(self):
     manage_button=self.click_element(self.manage_article)
     return manage_button

    # set search box
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_search_button(self,search):
        result_flag = self.set_text(self.search,search)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%search,
            negative='Failed to set the url in the form',
            level='debug')

    # click delete button 
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_delete_button(self):
     add_button=self.click_element(self.delete)
     return add_button  

    # click cancel button 
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_cancel_button(self):
     add_button=self.click_element(self.edit_cancel)
     return add_button 
            
     