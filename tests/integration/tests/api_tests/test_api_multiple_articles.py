"""
API TEST
Add articles in all categories - POST request(without url_params)

"""

import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from endpoints.API_Player import API_Player
from conf import api_tests_conf as conf
from conftest import interactivemode_flag
import time

@pytest.mark.API
def test_api_example(test_api_obj):
    "Run api test"
    try:
        expected_pass = 0
        actual_pass = -1

        # set authentication details
        headers = conf.headers
        article_editors = conf.article_editors

        # add articles
        for counter,editor in enumerate(article_editors):
            current_timestamp =str(int(time.time())+counter)
            counter += 1
            StrCounter = str(counter)
            article_details = {'url':conf.article_url +current_timestamp,'title':conf.article_title+StrCounter,'description':conf.article_description+StrCounter,'category_id':StrCounter,'article_editor':editor}
            response = test_api_obj.add_article(article_details=article_details,
                                                headers=headers)

            result_flag = True if 'Record' in response.get('response',{}).get('message','fail') else False
            test_api_obj.log_result(result_flag,
                                    positive='Successfully added new article with details %s' % response,
                                    negative='Could not add new article with details %s' % response)   
        
        # write out test summary
        expected_pass = test_api_obj.total
        actual_pass = test_api_obj.passed
        test_api_obj.write_test_summary()

    except Exception as e:
        print(e)
        test_api_obj.write("Exception when trying to run test:%s" % __file__)
        test_api_obj.write("Python says:%s" % str(e))

    # Assertion
    assert expected_pass == actual_pass,"Test failed: %s"%__file__

if __name__ == '__main__':
    test_api_example()
