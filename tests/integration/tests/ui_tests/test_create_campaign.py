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
from page_objects.form_object_create_newsletter import Form_Object_Create_Newsletter

@pytest.mark.GUI
def test_create_campaign(test_obj):

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
        
        #Get the test details from the conf file and fill the forms
        article_list_create_newsletter = conf.article_list_create_newsletter
        article_list_create_newsletter_number = 1
        #Initalize form counter
        article_number = 1		  
        test_obj = PageFactory.get_page_object("add articles page", base_url=test_obj.base_url)
        articles_added = []
        #Collect form data
        for article in article_list_create_newsletter:
            url = article['url']+str(int(time.time()))
            title = article['title']+str(int(time.time()))
            description = article['description']
            runtime = article['runtime']
            category = article['category']
            articles_added.append({'url':url,'title':title,'category':category})

            msg ="\nReady to fill article number %d"%article_number
            test_obj.write(msg)            

            #Set and submit the article in one go
            result_flag = test_obj.submit_article(url,title,description,runtime,category)
            test_obj.log_result(result_flag,
                                positive="Successfully submitted the article number %d\n"%article_number,
                                negative="Failed to submit the article number %d \nOn url: %s"%(article_number,test_obj.get_current_url()),
                                level="critical")
            test_obj.write('Script duration: %d seconds\n'%(int(time.time()-start_time)))
            test_obj.click_addanother_article()
            article_number += 1
        
        #Get the test details from the conf file
        subject = conf.subject
        opener = conf.opener
        preview = conf.preview

        #Create a test object for create newsletter
        test_obj = PageFactory.get_page_object("create newsletter page", base_url=test_obj.base_url) 
        #Collect form data
        for add_article in articles_added:
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
    