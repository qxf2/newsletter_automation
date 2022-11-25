from re import search
import conf.manage_articles_locator_conf as locators
from utils.Wrapit import Wrapit

class Table_Object:
    #get the edit locator
    edit =locators.edit
    #get the edit_url locator
    edit_url =locators.edit_url
    #get the edit_title locator
    edit_title =locators.edit_title
    #get the edit_description locator
    edit_description=locators.edit_description
    #get the edit_time locator
    edit_time=locators.edit_time
    #get the edit_category locator
    edit_category=locators.edit_category
    #get the edit_save locator
    edit_save=locators.edit_save
    #get the edit_cancel locator
    edit_cancel=locators.edit_cancel
    #get the delete locator
    delete =locators.delete

    def click_edit_button(self):
     add_button=self.click_element(self.edit)
     return add_button  
    
    def set_url(self,url):
        result_flag = self.set_text(self.edit_url,url)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url,
            negative='Failed to set the url in the form',
            level='debug')        

    def set_title(self,title):
        result_flag = self.set_text(self.edit_title,title)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title,
            negative='Failed to set the url in the form',
            level='debug')

    def set_description(self,description):
        result_flag = self.set_text(self.edit_description,description)
        self.conditional_write(result_flag,
            positive='Set the description to: %s'%description,
            negative='Failed to set the description in the form',
            level='debug')        
     
    def set_time(self,runtime):
        result_flag = self.set_text(self.edit_time,runtime)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime,
            negative='Failed to set the time in the form',
            level='debug')

    def set_category(self,category):
        result_flag = self.select_dropdown_option(self.edit_category,category)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category,
            negative='Failed to set the category in the form',
            level='debug')                
      
    #click the close button
    def click_save_button(self):
     submit_button=self.click_element(self.edit_save)
     return submit_button

    def click_delete_button(self):
     add_button=self.click_element(self.delete)
     return add_button  

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def edit_articles(self,url,title,description,runtime,category):
        "Submit the article"
        result_flag = self.click_edit_button()
        result_flag = self.set_url(url)
        result_flag = self.set_title(title)
        result_flag = self.set_description(description)
        result_flag = self.set_time(runtime)
        result_flag = self.set_category(category)
        result_flag = self.click_save_button()        

