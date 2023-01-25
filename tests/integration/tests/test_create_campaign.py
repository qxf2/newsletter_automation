"""
This is an example automated test to newsletter generator application
Our automated test will do the following:
    #Open Qxf2 newsletter generator application
    #Fill the details of create newsletter section.
"""
import os,sys,time
from typing_extensions import runtime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from page_objects.PageFactory import PageFactory
from utils.Option_Parser import Option_Parser
import conf.create_newsletter_conf as conf
import pytest

@pytest.mark.GUI
def test_create_campaign(test_obj):

    "Run the test"
    #try:
    if True:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        #Create a test object for edit an article
        test_obj = PageFactory.get_page_object("create newsletter page")
        #Set start_time with current time
        start_time = int(time.time())
        
        #Get the test details from the conf file
        email = conf.email
        password = conf.password
        title = conf.title
        category = conf.category
        subject = conf.subject
        opener = conf.opener
        preview = conf.preview
        
        #Create Newsletter
        result_create_newsletter = test_obj.create_newsletter(category,title)
        test_obj.log_result(result_create_newsletter,
        positive="The create newsletter is created successfully",
        negative="The create newsletter is not created successfully")

        #Set create newsletter subject
        result_newsletter_details_subject = test_obj.add_create_newsletter_subject(subject)
        test_obj.log_result(result_newsletter_details_subject,
        positive="The create newsletter subject is filled",
        negative="The create newsletter subject is not filled") 

        #Set create newsletter opener
        result_newsletter_details_opener = test_obj.add_create_newsletter_opener(opener)
        test_obj.log_result(result_newsletter_details_opener,
        positive="The create newsletter opener is filled",
        negative="The create newsletter opener is not filled")   

        #Set create newsletter preview
        result_newsletter_details_preview = test_obj.add_create_newsletter_preview(preview)
        test_obj.log_result(result_newsletter_details_preview,
        positive="The create newsletter preview is filled",
        negative="The create newsletter preview is not filled")               

        #click preview newsletter
        click_preview_newsletter = test_obj.click_preview_newsletter()
        test_obj.log_result(click_preview_newsletter,
        positive="The preview newsletter is clicked",
        negative="The preview newsletter is not clicked")                 

        #create campaign
        result_create_campaign = test_obj.create_campaign()      
        test_obj.log_result(result_create_campaign,
        positive="Campaign is succesfully created",
        negative="Campaign is not created")              

    #except Exception as e:
        #print("Exception when trying to run test: %s"%__file__)
        #print("Python says:%s"%str(e))

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