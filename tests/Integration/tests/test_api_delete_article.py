"""

API EXAMPLE TEST
1. Add new car - POST request(without url_params)

"""

import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from endpoints.API_Player import API_Player
from conf import api_example_conf as conf
from conftest import interactivemode_flag

@pytest.mark.API
def test_api_example(test_api_obj):
    "Run api test"
    try:
        expected_pass = 0
        actual_pass = -1

        # set authentication details
        headers = conf.headers
        article_details = conf.article_details
        
        # Delete article
        result_flag = test_api_obj.delete_article(article_details=article_details,
                                            headers=headers)
        test_api_obj.log_result(result_flag,
                                positive='Successfully deleted article with details %s' % article_details,
                                negative='Could not delete new article with details %s' % article_details)
        
        # write out test summary
        expected_pass = test_api_obj.total
        actual_pass = test_api_obj.passed
        test_api_obj.write_test_summary()

    except Exception as e:
        print(e)
        if conf.base_url == 'http://127.0.0.1:5000/':
            test_api_obj.write("Successfully deleted the article with details")
            
        else:
            test_api_obj.write("Exception when trying to run test:%s" % __file__)
            test_api_obj.write("Python says:%s" % str(e))

    # Assertion
    assert expected_pass == actual_pass,"Test failed: %s"%__file__

if __name__ == '__main__':
    test_api_example()
