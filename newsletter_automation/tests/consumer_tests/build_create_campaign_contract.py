""" Add consumer pact tests to create campaign mocking mailchimp provider"""
import requests, json, os
import logging
import atexit
import unittest
from pact import Consumer, Provider

PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 1234
PACT_DIR = os.path.dirname(os.path.realpath(__file__))

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def pact_session():
    """create pact session"""
    pact = Consumer('newsletter').has_pact_with(Provider('mailchimp'))
    try:
        pact.start_service()
    finally:  
        atexit.register(pact.stop_service)
    return pact

def create_campaign(request):
    """create a campaign on the mailchimp and return campaign id"""
    uri = 'http://{host_name}:{port}/create_campaign'.format(host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT, pact_dir="./pacts", log_dir="./logs")
    req = json.dumps(request)
    return requests.post(uri, data=req, headers = {'content-type': 'application/json'}).json()

class createCampaignContract(unittest.TestCase):
    """ pact test to build the contract """
    def test_create_campaign(self):
        request = {'title': 'The informed tester\'s newsletter', 'in_this_issue': 'To validate or verify pact tests','preview':'To validate or verify pact tests', 
                   'comic': {'comic_url': 'https://www.monkeyuser.com/2021/outcome-variables/', 'comic_text': 'Outcome variables'},
                   'this_week_articles': [{'title':'To Validate or Verify','url':'https://saucelabs.com/blog/to-validate-or-verify','description':'This article gives you the difference between validate and verify and also the importance of the same.','reading_time':'3 minutes'}],
                   'past_articles':[{'title':'Remote Video Interviews – A Guide For Improving Their Accuracy: ','url':'https://drjohnsullivan.com/articles/remote-video-interviews-guide-for-improving-their-accuracy/%7D','description':'Read this article to get some good tips on conduction Remote interviews.','reading_time':'8 minutes'}],
                   'automation_corner':[{'title':'Mutation Testing - The Most Comprehensive Way to Test Your Software:','url':'https://medium.com/swlh/mutation-testing-the-most-comprehensive-way-to-test-your-software-674f645bfc21','description':'Read this article to understand Mutation testing and how it can help you to understand the quality of the tests written','reading_time':'6 minutes'}]}
        response = {'campaign_id':100,
                   'title': 'The informed tester\'s newsletter', 'in_this_issue': 'To validate or verify pact tests','preview':'To validate or verify pact tests', 
                   'comic': {'comic_url': 'https://www.monkeyuser.com/2021/outcome-variables/', 'comic_text': 'Outcome variables'},
                   'this_week_articles': [{'title':'To Validate or Verify','url':'https://saucelabs.com/blog/to-validate-or-verify','description':'This article gives you the difference between validate and verify and also the importance of the same.','reading_time':'3 minutes'}],
                   'past_articles':[{'title':'Remote Video Interviews – A Guide For Improving Their Accuracy: ','url':'https://drjohnsullivan.com/articles/remote-video-interviews-guide-for-improving-their-accuracy/%7D','description':'Read this article to get some good tips on conduction Remote interviews.','reading_time':'8 minutes'}],
                   'automation_corner':[{'title':'Mutation Testing - The Most Comprehensive Way to Test Your Software:','url':'https://medium.com/swlh/mutation-testing-the-most-comprehensive-way-to-test-your-software-674f645bfc21','description':'Read this article to understand Mutation testing and how it can help you to understand the quality of the tests written','reading_time':'6 minutes'}]}        
        
        pact = pact_session()
        (pact.given('create campaign')
             .upon_receiving('a request to create campaign')
             .with_request(method='post',path='/create_campaign', body=request, headers = {'content-type': 'application/json'})
             .will_respond_with(status=200,body=response,headers = {'content-type': 'application/json'}))
        
        with pact:
            result = create_campaign(request)
        self.assertEqual(result, response)
        
if __name__ == "__main__":
    unittest.main(verbosity=2)