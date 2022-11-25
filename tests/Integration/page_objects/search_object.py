from re import search
import conf.manage_articles_locator_conf as locators
from utils.Wrapit import Wrapit

class Search_Object:
    #get the manage articles locator
    manage_article=locators.manage_article
    #get the search locator
    search =locators.search
    
    #set search box
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def search_word(self,search):
        result_flag = self.set_text(self.search,search)
        self.conditional_write(result_flag,
            positive='successfully Set the search: %s'%search,
            negative='Failed to set the search in the application',
            level='debug')    