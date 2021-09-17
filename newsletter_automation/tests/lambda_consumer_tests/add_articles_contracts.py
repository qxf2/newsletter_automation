"""Add pact tests to create contracts for add articles api call
add articles is provided by newsletter and consumed by lambda """

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import requests
import json
import logging
import atexit
import unittest
from pact import Consumer, Provider
import pdb
import uuid
#from  pactverify . matchers  import  Matcher , Like


PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 1234
PACT_DIR = os.path.dirname(os.path.realpath(__file__))

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def pact_session():
    """create pact session"""
    pact = Consumer('articlesLambda').has_pact_with(
        Provider('newsletterAutomation'))
    try:
        pact.start_service()
    finally:
        atexit.register(pact.stop_service)
    return pact


def add_articles(request):
    """Mocking the add articles api call"""
    uri = 'http://{host_name}:{port}/api/articles'.format(
        host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT, pact_dir="./pacts", log_dir="./logs")
    req = json.dumps(request)
    # add articles call needs x-api-key value from request
    headers = {'x-api-key': os.environ.get('API_KEY_VALUE',''), 'Content-Type': 'multipart/form-data'}

    return requests.post(uri, data=req, headers=headers)


class addArticlesContract(unittest.TestCase):

    def test_add_articles(self):
        """ pact test to build the contract """
        payload = {'url': 'https://uniquetesturl/{}'.format(str(uuid.uuid4())),
                   'category_id': 2, 'title': 'Test Title',
                   'description': 'Test Description',
                   'time': 5}
        response_text = 'Result of addition : Record added Successfully'
        # this test adds null x-api-key value to the contract json file
        # we need to update the api key value by following method for provider to execute the contract tests
        pact = pact_session()
        (pact.given('Found articles to add')
             .upon_receiving('a request to add article')
             .with_request(method='post', path='/api/articles', body=json.dumps(payload), headers={'x-api-key': os.environ.get('API_KEY_VALUE',''), 'Content-Type': 'multipart/form-data'})
             .will_respond_with(status=200, headers={'Content-Type':'text/html; charset=utf-8'}))

        with pact:
            result = add_articles(payload)
        self.assertEqual(result.status_code, 200)

def updateAPIKey():
    """update os.get.env(api_key) value in the json contract file"""
    with open("articleslambda-newsletterautomation.json","r") as contract_in:
        contract_data = json.load(contract_in)
        contract_data['interactions'][0]['request']['headers']['x-api-key'] = os.environ.get('API_KEY_VALUE','')
        contract_in.close()
    with open("articleslambda-newsletterautomation.json","w+") as contract_out:
        contract_out.write(json.dumps(contract_data,indent=4))
        contract_out.close()

if __name__ == "__main__":
    """Run contract tests which will create contract .json file then update api key value for provider execution """
    unittest.main(verbosity=2)
    updateAPIKey()
    # provider pact verification example command
    # pact-verifier --provider-base-url=http://localhost:5000 --pact-url=./articleslambda-newsletterautomation.json
