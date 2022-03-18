from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import conf.google_login_conf as login_conf


gmailID = login_conf.GMAILID
passWord = login_conf.PASSWORD

class Login():

    def setup(self):

        try:
            gmailID = login_conf.GMAILID
            passWord = login_conf.PASSWORD
            options = Options()
            options.headless = True
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ve')
            screenshot_name = "screenshots/my_screenshot_name.png"
            self.driver = webdriver.Chrome(options=options)
            self.driver.get((r'https://accounts.google.com/signin/v2/identifier?continue='+\
            'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
            '&flowName=GlifWebSignIn&flowEntry = ServiceLogin'))
            print("Headless Chrome Initialized")
            print("Page Title is : %s" % self.driver.title)

            loginBox = self.driver.find_element_by_xpath('//input[@type="email"]')
            loginBox.click()
            loginBox.clear()
            loginBox.send_keys(gmailID)

            self.driver.implicitly_wait(15)
            wait = WebDriverWait(self.driver, 60)
            waiting = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='identifierNext']")))
            nextbutton = self.driver.find_element_by_xpath('//div[@id="identifierNext"]')
            print("Next button found")
            nextbutton.click()
            print("Next button clicked")
            self.driver.implicitly_wait(10)
            print("Page Title is : %s" % self.driver.title)
            

        except Exception as e:

            print(e)

    def teardown(self):

        self.driver.quit()


class TestAddArticle():

    def test_add_article_headless_chrome(self):
        """
        Test class and methods
        """
        Login_obj=Login()
        Login_obj.setup()
        Login_obj.teardown()
