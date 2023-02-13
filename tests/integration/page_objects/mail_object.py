import conf.mail_locators_conf as locators
from utils.Wrapit import Wrapit
import time

class Mail_Object:
    "Page Object for the newsletter main page"
    #get the try_again locator
    try_again=locators.try_again
    #set the mail locator
    setting_mail=locators.setting_mail
    #set password locator
    password=locators.password
    #get nxt button locator
    nxt_button=locators.nxt_button
    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_try_again(self):
        "Start the SSO process"
        result_flag = self.click_element(self.try_again)
        self.conditional_write(result_flag,
            positive='Clicked the try again button to start the SSO process',
            negative='Could not click the try again button to begin the SSO process',
            level='debug')
        return result_flag

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.setting_mail,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')
        return result_flag
   
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_nxt_button(self):
        "Click the next button on the SSO screen"
        result_flag = self.click_element(self.nxt_button)
        self.conditional_write(result_flag,
            positive='Clicked the next button on the SSO screen',
            negative='Failed to click the next button on the SSO screen',
            level='debug')
        return result_flag
    
    #set the password
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self,password):
        result_flag = self.set_text(self.password,password)
        self.conditional_write(result_flag,
            positive='The password was set successfully',
            negative='Failed to set the password in the form',
            level='debug')
        return result_flag

    
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login(self,email,password):
        "Submit the article"
        result_flag = self.check_element_present(self.try_again)
        if result_flag:
            result_flag = self.click_try_again()
            result_flag &= self.set_email(email)
            result_flag &= self.click_nxt_button() 
            result_flag &= self.set_password(password)
            result_flag &= self.click_nxt_button() 
            return result_flag
        else:
            return True
