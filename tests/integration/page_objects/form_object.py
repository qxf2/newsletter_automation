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
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def home_hamburger(self):
        "Click the home link"
        result_flag = self.click_element(self.home)
        self.conditional_write(result_flag,
                                positive="Clicked on the Home nav button",
                                negative="Could not click on the Home button")
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_article(self):
        "Click the add articles button"
        add_button=self.click_element(self.add_articles)
        return add_button
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_url(self,url):
        "Set the URL in the add article form"
        result_flag = self.set_text(self.url,url)
        self.conditional_write(result_flag,
            positive='Set the url to: %s'%url,
            negative='Failed to set the url in the form',
            level='debug')
        return result_flag
     
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_title(self,title):
        "Set the title in the add article form"
        result_flag = self.set_text(self.title,title)
        self.conditional_write(result_flag,
            positive='Set the title to: %s'%title,
            negative='Failed to set the url in the form',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_description(self,description):
        "Set the description in the add article form"
        result_flag = self.set_text(self.description,description)
        self.conditional_write(result_flag,
            positive='Set the description to: %s'%description,
            negative='Failed to set the description in the form',
            level='debug')        
        return result_flag
     
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_time(self,runtime):
        "Set the time in the add article form"
        result_flag = self.set_text(self.time,runtime)
        self.conditional_write(result_flag,
            positive='Set the time to: %s'%runtime,
            negative='Failed to set the time in the form',
            level='debug')
        return result_flag
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_category(self,category):
        "Set category in the add article form"
        result_flag = self.select_dropdown_option(self.category,category)
        self.conditional_write(result_flag,
            positive='Set the category to: %s'%category,
            negative='Failed to set the category in the form',
            level='debug')    
        return result_flag            
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_submit(self):
        "Click the submit button of add article"
        result_flag = self.action_click(self.submit)
        self.conditional_write(result_flag,
            positive='Clicked submit on the add article form',
            negative='Could not click submit on the add article form',
            level='debug')    
        return result_flag
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_addanother_article(self):
        "Click the add another article button"
        result_flag = self.click_element(self.add_another_articles)
        self.conditional_write(result_flag,
                            positive='Clicked on the add another article link',
                            negative='Could not click on add another article link',
                            level='debug')
        return result_flag
   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def submit_article(self,url,title,description,runtime,category):
        "Submit the article"
        result_flag = self.set_url(url)
        result_flag &= self.set_title(title)
        result_flag &= self.set_description(description)
        result_flag &= self.set_time(runtime)
        result_flag &= self.set_category(category)
        result_flag &= self.click_submit()
        return result_flag
        