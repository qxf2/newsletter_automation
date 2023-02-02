import conf.add_articles_locators_conf as locators
import time
from utils.Wrapit import Wrapit

class Form_Object:
    #get home button locator
    home=locators.home
    #get the add articles locator
    add_articles=locators.add_articles
    #get the url  locator
    url=locators.url
    #get the title locator
    title=locators.title
    #get the description locator
    description=locators.description
    #get the time locator
    time =locators.time 
    #get the category locator
    category =locators.category
    #get the add_article locator
    submit =locators.submit
    #get the add_another_article locator 
    add_another_articles=locators.add_another_articles
    
    #click home
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def home_hamburger(self):
     click_home_hamburger=self.click_element(self.home)
     return click_home_hamburger

    #click add_article
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_article(self):
     add_button=self.click_element(self.add_articles)
     return add_button
    
    #set url
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_url(self,url):
        result_flag = self.set_text(self.url,url)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url,
            negative='Failed to set the url in the form',
            level='debug')
     
    #set title
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_title(self,title):
        result_flag = self.set_text(self.title,title)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title,
            negative='Failed to set the url in the form',
            level='debug')

    #set description
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_description(self,description):
        result_flag = self.set_text(self.description,description)
        self.conditional_write(result_flag,
            positive='Set the description to: %s'%description,
            negative='Failed to set the description in the form',
            level='debug')        
     
    #set time
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_time(self,runtime):
        result_flag = self.set_text(self.time,runtime)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime,
            negative='Failed to set the time in the form',
            level='debug')
    
    #set category
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_category(self,category):
        result_flag = self.select_dropdown_option(self.category,category)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category,
            negative='Failed to set the category in the form',
            level='debug')    
        return result_flag            
      
    #click the submit button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_submit(self):
     submit_button=self.click_element(self.submit)
     return submit_button
    
    #click add another article button       
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_addanother_article(self):
     addanother_article_button=self.click_element(self.add_another_articles)
     return addanother_article_button
   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_article(self,url,title,description,runtime,category):
        "Submit the article"
        result_flag = self.set_url(url)
        result_flag = self.set_title(title)
        result_flag = self.set_description(description)
        result_flag = self.set_time(runtime)
        result_flag = self.set_category(category)
        result_flag = self.click_submit()
        result_flag = self.click_addanother_article()

        return result_flag
