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
import conf.add_articles_conf as conf_add
import conf.create_newsletter_conf as conf
import pytest
from page_objects.form_object_create_newsletter import Form_Object_Create_Newsletter

@pytest.mark.GUI
def test_create_campaign(test_obj):

    "Run the test"
    try:
        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1
        #Create a test object for edit an article
        test_obj = PageFactory.get_page_object("add articles page", base_url=test_obj.base_url)
        #Set start_time with current time
        start_time = int(time.time())
        add_button = test_obj.click_add_article()
        #Get the test details from the conf file and fill the forms
        article_list_create_newsletter = conf.article_list_create_newsletter
        article_list_create_newsletter_number = 1
        #Initalize form counter
        article_number = 1		  
        
        #Collect form data
        for article in article_list_create_newsletter:
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
            test_obj = PageFactory.get_page_object("add articles page", base_url=test_obj.base_url)
            article_list_create_newsletter_number = article_list_create_newsletter_number + 1

            #Set and submit the article in one go
            result_flag = test_obj.submit_article(url,title,description,runtime,category)
            test_obj.log_result(result_flag,
                                positive="Successfully submitted the article number %d\n"%article_number,
                                negative="Failed to submit the article number %d \nOn url: %s"%(article_number,test_obj.get_current_url()),
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))

        #Get the test details from the conf file
        subject = conf.subject
        opener = conf.opener
        preview = conf.preview

        #Collect form data
        for add_article in article_list_create_newsletter:
            title = add_article['TITLE']
            category = add_article['CATEGORY']

            #Create a test object for create newsletter
            test_obj = PageFactory.get_page_object("create newsletter page", base_url=test_obj.base_url) 

            #select and add articles for all the categories
            result_flag = test_obj.add_articles(title,category)
            test_obj.log_result(result_flag,
                                positive="Successfully added the articles",
                                negative="Failed to add the articles",
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time))) 

        #set the subject,opener and preview details and click preview newsletter
        result_flag = test_obj.add_newsletter_details(subject,opener,preview)
        test_obj.log_result(result_flag,
                            positive="Successfully added the articles details and clicked on preview newsletter",
                            negative="Failed to add the articles details and click on preview newsletter",                                level="critical")
        test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))              

        #Create a test object for preview newsletter
        test_obj = PageFactory.get_page_object("preview newsletter page", base_url=test_obj.base_url)                        

        #create the campaign
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