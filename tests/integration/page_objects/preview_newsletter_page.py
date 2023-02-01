"""
This class models the newsletter preview newsletter page.

"""
from .Base_Page import Base_Page
from .mail_object import Mail_Object
from .form_object import Form_Object
from .hamburger_object import Hamburger_Object
import conf.preview_newsletter_conf as locators

class Previewnewsletter_Page(Base_Page, Mail_Object, Hamburger_Object, Form_Object):
    "Page Object for the newsletter preview page"

    #get the create campaign locator
    CREATE_NEWSLETTER_CREATE_CAMPAIGN = locators.CREATE_CAMPAIGN   

    #click create campaign button
    def create_campaign(self):
        self.scroll_down(self.CREATE_NEWSLETTER_CREATE_CAMPAIGN)
        result_create_campaign = self.click_element(self.CREATE_NEWSLETTER_CREATE_CAMPAIGN)
        self.conditional_write(result_create_campaign,
                                positive='The create campaign is clicked',
                                negative='The create campaign is not clicked',
                                level='debug')            
        return result_create_campaign 