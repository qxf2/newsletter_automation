from re import search
import conf.manage_articles_locator_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    # get the manage articles locator
    manage_article=locators.manage_article
    # get the search locator
    search =locators.search
    
    # click manage article button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_managearticle_button(self):
     manage_button=self.click_element(self.manage_article)
     return manage_button

    # set search box
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_search(self,search):
        result_flag = self.set_text(self.search,search)
        self.conditional_write(result_flag,
            positive='successfully Set the search: %s'%search,
            negative='Failed to set the search in the application',
            level='debug')

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_article(self,search):
        "Submit the article"
        result_flag = self.click_managearticle_button()
        result_flag = self.set_search(search)          

   