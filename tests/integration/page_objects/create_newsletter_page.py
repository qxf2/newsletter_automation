"""
This class models the newsletter main page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .form_object import Form_Object
from .hamburger_object import Hamburger_Object
import conf.create_newsletter_locator_conf as locators

class Createnewsletter_Page(Base_Page, Mail_Object, Hamburger_Object, Form_Object):
    "Page Object for the newsletter main page"

    #locators for create newsletter page
    CREATE_NEWSLETTER_SELECT_CATEGORY = locators.SELECT_CATEGORY
    CREATE_NEWSLETTER_URL = locators.CATEGORY_URL
    CREATE_NEWSLETTER_ADD_MORE_ARTICLE = locators.ADD_MORE_ARTICLE
    CREATE_NEWSLETTER_CLEAR_FIELDS = locators.CLEAR_FIELDS
    CREATE_NEWSLETTER_ADDED_ARTICLE = locators.ADDED_ARTICLE
    CREATE_NEWSLETTER_SELECT_URL = locators.SELECT_URL

    def start(self):
        "Use this method to go to specific URL -- if needed"
        url = 'create-newsletter'
        self.open(url)

    def create_newsletter(self,category,title):

        result_click_category = self.click_element(self.CREATE_NEWSLETTER_SELECT_CATEGORY%category)
        if result_click_category is True:
            self.write("The category %s is selected"%category)
        else:
            self.write("The category %s is not selected"%category)
        result_click_url = self.click_element(self.CREATE_NEWSLETTER_URL)
        result_select_url = self.click_element(self.CREATE_NEWSLETTER_SELECT_URL%title)
        if result_select_url is not None:
            self.write("The Title %s is present"%title)
        else:
            self.write("The Title %s is not present"%title)
        result_add_more_article = self.click_element(self.CREATE_NEWSLETTER_ADD_MORE_ARTICLE)
        self.scroll_down(self.CREATE_NEWSLETTER_CLEAR_FIELDS)
        check_added_article = self.get_text(self.CREATE_NEWSLETTER_ADDED_ARTICLE%title)
        if check_added_article is not None:
            self.write("The Title %s is added"%title)
        else:
            self.write("The Title %s is not added"%title) 
        return result_click_category  

    def create_campaign(self):
        self.scroll_down(self.CREATE_NEWSLETTER_CREATE_CAMPAIGN)
        result_create_campaign = self.click_element(self.CREATE_NEWSLETTER_CREATE_CAMPAIGN)
        if result_create_campaign is True:
            self.write("The create campaign is clicked")
        else:
            self.write("create campaign is not clicked")            
        return result_create_campaign         

            
