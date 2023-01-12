"""
This is an example automated test to newsletter generator application
Our automated test will do the following:
    #Open Qxf2 newsletter generator application
    #Fill the details of add articles section.
"""
import os,sys,time
from turtle import title
from typing_extensions import runtime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.add_articles_conf as conf
import pytest

@pytest.mark.GUI
def test_add_article(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        #Create a test object for add articles 
        test_obj = PageFactory.get_page_object("add articles page")
        #Set start_time with current time
        start_time = int(time.time())
        
        #Get the test details from the conf file
        email = conf.email
        password = conf.password
        
        #Set the login
        login = test_obj.login(email,password)
        #click the hamburger button
        hamburger_button = test_obj.click_hamburger_button()
        #click the add_articles button
        add_button = test_obj.click_add_article()
        #Get the test details from the conf file and fill the forms
        article_list = conf.article_list
        #Initalize form counter
        article_number = 1		  
        
        #Collect form data
        for article in article_list:
            url = article['URL']
            title = article['TITLE']
            description = article['DESCRIPTION']
            runtime = article['RUNTIME']
            category = article['CATEGORY']
            submit_button = test_obj.click_submit()
            add_another_article = test_obj.click_addanother_article()
           
            msg ="\nReady to fill article number %d"%article_number
            test_obj.write(msg)
           
            #Visit main page again
            test_obj = PageFactory.get_page_object("add articles page")
            article_number = article_number + 1

            #Set and submit the article in one go
            result_flag = test_obj.submit_article(url,title,description,runtime,category)
            test_obj.log_result(result_flag,
                                positive="Successfully submitted the article number %d\n"%article_number,
                                negative="Failed to submit the article number %d \nOn url: %s"%(article_number,test_obj.get_current_url()),
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
 
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__

#---START OF SCRIPT
if __name__=='__main__':
    print("Start of %s"%__file__)
    #Creating an instance of the class
    options_obj = Option_Parser()
    options = options_obj.get_options()

    #Run the test only if the options provided are valid
    if options_obj.check_options(options):
        test_obj = PageFactory.get_page_object("Zero",base_url=options.url)

        #Setup and register a driver
        test_obj.register_driver(options.remote_flag,options.os_name,options.os_version,options.browser,options.browser_version,options.remote_project_name,options.remote_build_name)

        #Setup TestRail reporting
        if options.testrail_flag.lower()=='y':
            if options.test_run_id is None:
                test_obj.write('\033[91m'+"\n\nTestRail Integration Exception: It looks like you are trying to use TestRail Integration without providing test run id. \nPlease provide a valid test run id along with test run command using -R flag and try again. for eg: pytest -X Y -R 100\n"+'\033[0m')
                options.testrail_flag = 'N'
            if options.test_run_id is not None:
                test_obj.register_testrail()
                test_obj.set_test_run_id(options.test_run_id)

        if options.tesults_flag.lower()=='y':
            test_obj.register_tesults()

        test_add_article(test_obj)

     #teardowm
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())
