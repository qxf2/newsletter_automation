import conf.create_newsletter_locator_conf as locators
import time
from utils.Wrapit import Wrapit

class Form_Object_Create_Newsletter:
    #get the create_newsletter subject locator
    CREATE_NEWSLETTER_SUBJECT = locators.SUBJECT
    #get the create_newsletter opener locator
    CREATE_NEWSLETTER_OPENER = locators.OPENER
    #get the create_newsletter preview locator
    CREATE_NEWSLETTER_PREVIEW_TEXT = locators.PREVIEW_TEXT
    #get the create_newsletter preview newsletter button locator
    CREATE_NEWSLETTER_PREVIEW_NEWSLETTER = locators.PREVIEW_NEWSLETTER
    #get the select category locator
    CREATE_NEWSLETTER_SELECT_CATEGORY = locators.SELECT_CATEGORY
    #get the url dropdown locator
    CREATE_NEWSLETTER_URL = locators.CATEGORY_URL
    #get the add more article button locator
    CREATE_NEWSLETTER_ADD_MORE_ARTICLE = locators.ADD_MORE_ARTICLE
    #get the clear fields locator
    CREATE_NEWSLETTER_CLEAR_FIELDS = locators.CLEAR_FIELDS
    #get the url locator
    CREATE_NEWSLETTER_SELECT_URL = locators.SELECT_URL

    #click the category dropdown
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_category(self,category):
        result_click_category = self.click_element(self.CREATE_NEWSLETTER_SELECT_CATEGORY%category)     
        self.conditional_write(result_click_category,
                                positive='The category %s is selected'%category,
                                negative='The category %s is not selected'%category,
                                level='debug')
        return result_click_category

    #click the url dropdown
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_url(self):
        result_click_url = self.click_element(self.CREATE_NEWSLETTER_URL)
        self.conditional_write(result_click_url,
                                positive='The url is clicked',
                                negative='The url is not clicked',
                                 level='debug')
        return result_click_url

    #select the url from the dropdown
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def select_url(self,title):
        result_select_url = self.click_element(self.CREATE_NEWSLETTER_SELECT_URL%title)
        self.conditional_write(result_select_url,
                                positive='The Title %s is present and clicked'%title,
                                negative='The Title %s is not present"%title',
                                level='debug')
        return result_select_url       

    #click add more article button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_add_more_article(self):
        result_add_more_article = self.click_element(self.CREATE_NEWSLETTER_ADD_MORE_ARTICLE)
        self.conditional_write(result_add_more_article,
                                positive='The add more article button is clicked',
                                negative='The add article button is not clicked',
                                level='debug')
        return result_add_more_article

    #scroll down to end of create newsletter page
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def scroll_down_create_newsletter(self):
        self.scroll_down(self.CREATE_NEWSLETTER_CLEAR_FIELDS)
        check_clear_fields = self.check_element_displayed(self.CREATE_NEWSLETTER_CLEAR_FIELDS)
        self.conditional_write(check_clear_fields,
                                positive='The page is scrolled down and the clear field button is visible',
                                negative='The page is not scrolled down',
                                level='debug')
        return check_clear_fields
 
    #set create newsletter subject
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_create_newsletter_subject(self,subject):
        result_add_subject = self.set_text(self.CREATE_NEWSLETTER_SUBJECT,subject)
        return result_add_subject        

    #set create newsletter opener
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_create_newsletter_opener(self,opener):    
        result_add_opener = self.set_text(self.CREATE_NEWSLETTER_OPENER,opener)
        return result_add_opener
    
    #set create newsletter preview
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_create_newsletter_preview(self,preview):     
        result_add_preview = self.set_text(self.CREATE_NEWSLETTER_PREVIEW_TEXT,preview)
        return result_add_preview 

    #click preview newsletter button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_preview_newsletter(self):
        result_preview_newsletter = self.click_element(self.CREATE_NEWSLETTER_PREVIEW_NEWSLETTER)
        self.conditional_write(result_preview_newsletter,
                                positive='The preview newsletter is clicked',
                                negative='The preview newsletter is not clicked',
                                level='debug')        
        return result_preview_newsletter

    #add articles in create newsletter
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def add_articles(self,title,category):
        "Add articles in Create newsletter"
        result_flag = self.click_category(category)
        result_flag = self.click_url()
        result_flag = self.select_url(title)
        result_flag = self.click_add_more_article()

        return result_flag

    #add newsletter details and click preview newsletter button
    def add_newsletter_details(self,subject,opener,preview):
        "Add newsletter details and click preview newsletter"
        result_flag = self.scroll_down_create_newsletter()
        result_flag = self.add_create_newsletter_subject(subject)
        result_flag = self.add_create_newsletter_opener(opener)
        result_flag = self.add_create_newsletter_preview(preview)
        result_flag = self.click_preview_newsletter()

        return result_flag        
