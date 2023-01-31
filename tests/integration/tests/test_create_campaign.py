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

            #Click the category dropdown
            result_click_category = test_obj.click_category(category)
            test_obj.log_result(result_click_category,
            positive="The category is clicked successfully",
            negative="The category is not clicked successfully")

            #Click the url dropdown
            result_click_url = test_obj.click_url()
            test_obj.log_result(result_click_url,
            positive="The url is clicked successfully",
            negative="The url is not clicked successfully")

            #Select the url from dropdown
            result_select_url = test_obj.select_url(title)
            test_obj.log_result(result_select_url,
            positive="The url is selected successfully",
            negative="The url is not selected successfully")    

            #Click add more article button
            result_click_add_more_article = test_obj.click_add_more_article()  
            test_obj.log_result(result_click_add_more_article,
            positive="The add more article button is clicked",
            negative="The add more article button is not clicked")        

        #Scroll down to end of create newsletter page
        result_scroll_down = test_obj.scroll_down_create_newsletter()
        test_obj.log_result(result_scroll_down,
        positive="The page is scrolled down",
        negative="The page is not scrolled. Please check the method")          

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

        #Create a test object for preview newsletter
        test_obj = PageFactory.get_page_object("preview newsletter page", base_url=test_obj.base_url)                        

        #create the campaign
        result_create_campaign = test_obj.create_campaign()      
        test_obj.log_result(result_create_campaign,
        positive="Campaign is succesfully created",
        negative="Campaign is not created")              

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__