"""
This is an accessibility test to newsletter generator application
Our automated test will do the following:
    #Open Qxf2 newsletter generator application
    #Run accessibility for every page
    #Create snapshot for each page
"""
import os
import sys
from page_objects.PageFactory import PageFactory
import conf.edit_articles_conf as conf
import pytest
from typing_extensions import runtime
from utils.Option_Parser import Option_Parser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

url = conf.url
title = conf.title
description = conf.description
runtime = conf.runtime
category = conf.category
search = conf.search

@pytest.mark.ACCESSIBILITY
def test_accessibility(test_obj, snapshot):
    "Inject Axe and create snapshot for every page"

    #Get all pages
    page_names = PageFactory.get_all_page_names()

    for page in page_names:
        test_obj = PageFactory.get_page_object(page,base_url=test_obj.base_url)
        if page == "edit articles page":
            #Set the search string
            test_obj.search_word(search)
            #Click the edit button
            test_obj.edit_articles(url,title,description,runtime,category)
            #Inject Axe
            test_obj.accessibility_inject_axe()
            print("Injected Axe in:" f"{page}")
            #Run Axe
            result = test_obj.accessibility_run_axe()
            print("Ran Axe in:" f"{page}")
            #Create Snapshot
            snapshot.assert_match(f"{result}", f'snapshot_output_{page}.txt')
        else:
            #Inject Axe
            test_obj.accessibility_inject_axe()
            print("Injected Axe in:" f"{page}")
            #Run Axe
            result = test_obj.accessibility_run_axe()
            print("Ran Axe in:" f"{page}")
            #Create Snapshot
            snapshot.assert_match(f"{result}", f'snapshot_output_{page}.txt')

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

        test_accessibility(test_obj)

     #teardowm
        test_obj.teardown()
    else:
        print('ERROR: Received incorrect comand line input arguments')
        print(option_obj.print_usage())         
