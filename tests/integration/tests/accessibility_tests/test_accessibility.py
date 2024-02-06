"""
This is a test file to run accessibility test on
    1. Newsletter login page
    2. Newsletter add article page
    3. Newsletter manage article page
    4. Newsletter edit article page
    5. Newsletter create newsletter page
"""
import os
import sys
import json
import re
import pytest
from page_objects.PageFactory import PageFactory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.mark.ACCESSIBILITY
def test_accessibility(test_obj):
    "Inject Axe and create snapshot for every page"
    try:

        #Initalize flags for tests summary
        expected_pass = 0
        actual_pass = -1

        #Get all pages
        page_names = PageFactory.get_all_page_names()

        for page in page_names:
            test_obj = PageFactory.get_page_object(page,base_url=test_obj.base_url)
            #Inject Axe in every page
            test_obj.accessibility_inject_axe()
            #Check if Axe is run in every page
            run_result = test_obj.accessibility_run_axe({
                'exclude': ['table']
            })
            #Serialize dict to JSON-formatted string
            result_str = json.dumps(run_result, ensure_ascii=False, separators=(',', ':'))
            #Formatting result by removing \n,\\,timestamp
            #Every test run have a different timestamp.
            cleaned_result = re.sub(r'\\|\n|\r|"timestamp":\s*"[^"]*"', '', result_str)
            if page == 'add articles page':
                #removing csrf_token from add article page
                cleaned_result = re.sub(r'name\s*=\s*"csrf_token"\s*value\s*=\s*"[^"]*"', '', cleaned_result)
            if page == "create newsletter page":
                #removing csrf_token from create newsletter page
                cleaned_result = re.sub(r'name\s*=\s*"csrf_token"(?:\s*type\s*=\s*"hidden")?\s*value\s*=\s*"[^"]*"', '', cleaned_result)
            #Compare Snapshot for each page
            #snapshot_result = test_obj.snapshot_assert_match(f"{cleaned_result}",
            #                                                 f'snapshot_output_{page}.txt')

            # Create a filename based on the page name
            filename = f'{page}_output.txt'
            print(filename)
            print(cleaned_result)

            # filename = f'{page}_output.txt'

            # # Open the file in write mode
            # with open(filename, 'w', encoding='utf-8') as file:
            #     file.write(cleaned_result)

            #test_obj.log_result(snapshot_result,
            #                    positive=f'Accessibility checks for {page} passed',
            #                    negative=f'Accessibility checks for {page} failed')

        #Print out the result
        test_obj.write_test_summary()
        expected_pass = test_obj.result_counter
        actual_pass = test_obj.pass_counter

    except Exception as e:
        print("Exception when trying to run test: %s"%__file__)
        print("Python says:%s"%str(e))

    assert expected_pass == actual_pass, "Test failed: %s"%__file__
