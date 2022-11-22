import conf.mail_locators_conf as locators
from utils.Wrapit import Wrapit
import time
class Mail_Object:
    "Page Object for the interview scheduler main page"
    # get the try_again locator
    try_again=locators.try_again
    # get the sign_in locator
    sign_in=locators.sign_in
    # set the mail locator
    setting_mail=locators.setting_mail
    # set password locator
    password=locators.password
    # get nxt button locator
    nxt_button=locators.nxt_button
    
    # click the try again button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_try_again(self):
     try_again_button=self.click_element(self.try_again)
     return try_again_button

    #click the sign in button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_sign_in(self):
     sign_in_button=self.click_element(self.sign_in)
     return sign_in_button
    
    # set the email 
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_email(self,email):
        "Set the email on the form"
        result_flag = self.set_text(self.setting_mail,email)
        self.conditional_write(result_flag,
            positive='Set the email to: %s'%email,
            negative='Failed to set the email in the form',
            level='debug')
   
    #click the next button
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def click_nxt_button(self):
     Button=self.click_element(self.nxt_button)
     return Button 
    
    # set the password
    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def set_password(self,password):
        result_flag = self.set_text(self.password,password)
        self.conditional_write(result_flag,
            positive='The password was set successfully',
            negative='Failed to set the password in the form',
            level='debug')

    @Wrapit._exceptionHandler
    @Wrapit._screenshot
    def login_page(self,email,password):
        "Submit the article"
        result_flag = self.click_try_again()
        result_flag = self.click_sign_in()
        result_flag = self.set_email(email)
        result_flag = self.click_nxt_button() 
        result_flag = self.set_password(password)
        result_flag = self.click_nxt_button() 
         
 