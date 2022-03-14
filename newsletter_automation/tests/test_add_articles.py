from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import conf.google_login_conf as login_conf


gmailID = login_conf.GMAILID
passWord = login_conf.PASSWORD

def test_add_article():
    """
    This function will test add articles to the newsletter
    """
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)

        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(gmailID)

        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)

        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()
        driver.implicitly_wait(15)


        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
        driver.implicitly_wait(15)
        driver.get('https://newsletter-generator.qxf2.com/')

        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//a[text()='Sign in']").click()

        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//div[@data-email='test@qxf2.com']").click()

        driver.implicitly_wait(180)
        driver.find_element_by_xpath(" //div[contains(@class, 'header-header') and contains(.//h1, 'Qxf2 Services Newsletter Generator')]").is_displayed()

        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//a[text()='articles']").click()

        driver.implicitly_wait(15)
        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

        driver.implicitly_wait(15)
        driver.get('https://newsletter-generator.qxf2.com/articles')

        driver.implicitly_wait(15)
        driver.find_element_by_xpath("//h2[contains(text(),'Add ')]").is_displayed()
        driver.implicitly_wait(200)

        url = driver.find_elements_by_xpath('//*[@id ="url"]')
        url[0].send_keys('https://qxf2.com/')
        driver.implicitly_wait(15)

        title = driver.find_elements_by_xpath('//*[@id ="title"]')
        title[0].send_keys('Qxf2 Services Newsletter Generator')
        driver.implicitly_wait(15)

        description = driver.find_elements_by_xpath('//*[@id ="description"]')
        description[0].send_keys('Qxf2 Services Newsletter Generator')
        driver.implicitly_wait(30)

        time = driver.find_elements_by_xpath('//*[@id ="time"]')
        time[0].send_keys(10)
        driver.implicitly_wait(15)

        category_id = driver.find_elements_by_xpath('//*[@id ="category_id"]')
        category_id[0].send_keys('pastweek')
        driver.implicitly_wait(15)

        submit= driver.find_elements_by_xpath('//*[@id ="submit"]')
        submit[0].click()
        driver.implicitly_wait(180)

        success = driver.find_elements_by_xpath('//a[text()="Go back to articles page"]')
        success[0].is_displayed()

        print('Article added...!!')

        logout = driver.find_elements_by_xpath('//button[@type="button" and contains(text(),"Logout")]')
        logout[0].click()

        print('Logged Out...!!')

    except:
        print('Login Failed')