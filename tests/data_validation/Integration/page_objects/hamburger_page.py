import conf.hamburger_locators as locators
class Hamburger_Object_Page:
    
    # get the hamburger locator
    hamburger=locators.hamburger
   
    def click_hamburger_button(self):
     hamburger_button=self.hover(self.hamburger)
     return hamburger_button    

    
            
     