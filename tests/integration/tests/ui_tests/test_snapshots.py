"""
This is an example automated test to newsletter generator application that uses percy to take snapshots of different pages of the application, so as to perform snapshot testing.
"""
import os,sys,time
from typing_extensions import runtime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.create_newsletter_conf as conf
import pytest
from page_objects.form_object_create_newsletter import Form_Object_Create_Newsletter
from percy import percy_snapshot

@pytest.mark.GUI
def test_snapshot(test_obj):
    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        start_time = int(time.time())

        #Get the test details from the conf file
        email = conf.email
        password = conf.password

        test_obj = PageFactory.get_page_object("Login", base_url=test_obj.base_url)
        result_flag = test_obj.login(email, password)
        test_obj.log_result(result_flag, 
                            positive = "Logged into the app", 
                            negative = "Could not log in to the app")
        #Snapshot of homepage
        percy_snapshot(driver=test_obj.get_current_driver(),name="Homepage")
        
        #Get the test details from the conf file and fill the forms
        article_list_create_newsletter = conf.article_list_create_newsletter
        article_list_create_newsletter_number = 1
        #Initalize form counter
        article_number = 1		  
        test_obj = PageFactory.get_page_object("add articles page", base_url=test_obj.base_url)
        #Snapshot of add article page
        percy_snapshot(driver=test_obj.get_current_driver(),name="Add article page")

        #Collect form data
        for article in article_list_create_newsletter:
            url = article['url']
            title = article['title']
            description = article['description']
            runtime = article['runtime']
            category = article['category']

            msg ="\nReady to fill article number %d"%article_number
            test_obj.write(msg)            

            #Set and submit the article in one go
            result_flag = test_obj.submit_article(url,title,description,runtime,category)
            test_obj.log_result(result_flag,
                                positive="Successfully submitted the article number %d\n"%article_number,
                                negative="Failed to submit the article number %d \nOn url: %s"%(article_number,test_obj.get_current_url()),
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
            if article_number==1:
                #Snapshot of add another article page
                percy_snapshot(driver=test_obj.get_current_driver(),name="Add another article page", percy_css='div p:nth-child(1) {visibility:hidden; }')

            test_obj.click_addanother_article()

            article_number += 1
        
        #Get the test details from the conf file
        subject = conf.subject
        opener = conf.opener
        preview = conf.preview

        #Manage article page
        test_obj = PageFactory.get_page_object("edit articles page",base_url=test_obj.base_url)
        #Snapshot of manage articles page
        percy_snapshot(driver=test_obj.get_current_driver(),name="Manage article page", percy_css='tbody {visibility:hidden; }')


        #Create a test object for create newsletter
        test_obj = PageFactory.get_page_object("create newsletter page", base_url=test_obj.base_url)

        #snapshot of create campaign page
        percy_snapshot(driver=test_obj.get_current_driver(),name="Create campaign page")

        #Collect form data
        for add_article in article_list_create_newsletter:
            title = add_article['title']
            category = add_article['category']
            
            #Select and add articles for all the categories
            result_flag = test_obj.add_articles(title,category)
            test_obj.log_result(result_flag,
                                positive="Successfully added the articles",
                                negative="Failed to add the articles",
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        #Set the subject,opener and preview details and click preview newsletter
        result_flag = test_obj.add_newsletter_details(subject,opener,preview)
        test_obj.log_result(result_flag,
                            positive="Successfully added the articles details and clicked on preview newsletter",
                            negative="Failed to add the articles details and click on preview newsletter",
                            level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))              

        #Create a test object for preview newsletter
        test_obj = PageFactory.get_page_object("preview newsletter page", base_url=test_obj.base_url)
        #snapshot of preview article page
        percy_snapshot(driver=test_obj.get_current_driver(),name="Preview article page", percy_css='tbody td {visibility:hidden; }')

        #Create the campaign
        result_create_campaign = test_obj.create_campaign()      
        test_obj.log_result(result_create_campaign,
                            positive="Campaign is succesfully created",
                            negative="Campaign is not created")     
        
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

        test_snapshot(test_obj)

     #teardowm
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())