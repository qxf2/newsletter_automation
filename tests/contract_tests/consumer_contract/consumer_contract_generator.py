"""
The following code is used to generate pact consumer contract for newsletter application
"""
import atexit
import unittest
import requests
from pact import Consumer, Provider
import os
import json

#Set the Consumer and Provider. Newsletter Lambda is our Consumer and Newsletter API is our Provider
pact = Consumer('NewsletterLambda').has_pact_with(Provider('NewsletterAPI'), pact_dir='./pacts')

pact.start_service()

atexit.register(pact.stop_service)


class NewsletterApiTest(unittest.TestCase):

    def _request_helper(self, path, data):
        return requests.post(pact.uri + path, data = json.loads(json.dumps(data)))

    def test_post_new_articles(self):
        "Generate contract condition for additon of new articles through the Newsletter API"
        path = '/api/articles'
        data = "url=www.new-article.com&category_id=5&article_editor=Pact_tester"
        expected_body = {'message': 'Record added successfully'}
        expected_status = 200
          
        (pact
         .given('post new article to database')
         .upon_receiving('a request to post new article')
         .with_request(method='post',path=path,body=data)
         .will_respond_with(expected_status, body=expected_body))

        with pact:
          resp = self._request_helper(path,data)
        
        self.assertEqual(resp.status_code, expected_status)
        self.assertEqual(resp.json(), expected_body)

    def test_post_existing_articles(self):
        "Generate contract condition for additon of existing  articles through the Newsletter API"
        path = '/api/articles'
        data = "url=www.existing-article.com&category_id=5&article_editor=Pact_tester"
        expected_body = {'message': 'URL already exists in database'}
        expected_status = 200
          
        (pact
         .given('post existing article to database')
         .upon_receiving('a request to post an existing article')
         .with_request(method='post',path=path,body=data)
         .will_respond_with(expected_status, body=expected_body))

        with pact:
          resp = self._request_helper(path,data)
        
        self.assertEqual(resp.status_code, expected_status)
        self.assertEqual(resp.json(), expected_body)


    


       

