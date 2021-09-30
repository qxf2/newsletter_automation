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
provider = 'newsletterautomation'
consumer = 'articleslambda'

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def pact_session():
    """create pact session"""
    pact = Consumer(consumer).has_pact_with(
        Provider(provider))
    try:
        pact.start_service()
    finally:
        atexit.register(pact.stop_service)
    return pact


def add_articles(request):
    """Mocking the add articles api call"""
    uri = 'http://{host_name}:{port}/api/articles'.format(
        host_name=PACT_MOCK_HOST, port=PACT_MOCK_PORT, pact_dir="./pacts", log_dir="./logs")
    # add articles call needs x-api-key value from request
    headers = {'x-api-key': os.environ.get('API_KEY',''),'Content-Type':'application/json'}

    return requests.post(uri, headers=headers, data=request)


class addArticlesContract(unittest.TestCase):

    def test_add_articles(self):
        """ pact test to build the contract between lambda consumer and newsletter provider """
        payload = {"url": "https://uniquetesturl/{}".format(str(uuid.uuid4())),
                   "category_id": "2",
                   "title": "Test Title",
                   "description": "Test Description",
                   "time": "5"}

        expected = {'msg': 'Record added Successfully'}

        # this test adds null x-api-key value to the contract json file
        # we need to update the api key value by following method for provider to execute the contract tests
        pact = pact_session()
        (pact.given('Found articles to add')
             .upon_receiving('a request to add article')
             .with_request(method='post', path='/api/articles', body=payload, headers={'x-api-key': os.environ.get('API_KEY',''),'Content-Type':'application/json'})
             .will_respond_with(status=200, headers={'Content-Type':'application/json'},body=expected))

        with pact:
            payload = json.dumps(payload)
            result = add_articles(payload)

        self.assertEqual(result.status_code, 200)

def updateAPIKey():
    """update os.get.env(api_key) value in the json contract file"""
    contract_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"{}-{}.json".format(consumer,provider))
    #run this consumer tests from tests folder to get the contract file created under tests file
    if os.path.exists(contract_file):
        with open(contract_file,"r+") as contract_in:
            pdb.set_trace()
            contract_data = json.load(contract_in)
            contract_data['interactions'][0]['request']['headers']['x-api-key'] = os.environ.get('API_KEY','')
            contract_in.close()
        with open(contract_file,"w+") as contract_out:
            contract_out.write(json.dumps(contract_data,indent=4))
            contract_out.close()
    else:
        print("{} file not found".format(contract_file))

if __name__ == "__main__":
    """Run contract tests which will create contract .json file then update api key value for provider execution """
    unittest.main(verbosity=2)
    pact_contract = addArticlesContract
    pact_contract.test_add_articles()
    updateAPIKey()

    # provider pact verification example command
    # pact-verifier --provider-base-url=http://localhost:5000 --pact-url=./articleslambda-newsletterautomation.json
