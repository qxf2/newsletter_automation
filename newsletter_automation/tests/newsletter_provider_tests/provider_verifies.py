""" when any changes to provider apis, provider needs to run contracts and check if its breaking any consumer
can verify contracts using pact verifier CLI >> pact-verifier --provider-base-url=http://localhost:port --pact-url=./contract.json
or using python pact verifier lib
"""

import logging
import os,sys
from pact.verifier import Verifier
import pytest
import pdb
from argparse import ArgumentParser

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
"""
provider = 'newsletterAutomation'
consumer = 'articlesLambda'
PACT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"{}-{}.json".format(consumer,provider))
PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 5000
PACT_BASE_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)
PACT_DIR = os.path.dirname(os.path.realpath(__file__))
BROKER_URL = 'https://qxf2services.pactflow.io/'
"""
provider = 'newsletterautomation'
consumer = 'articleslambda'
broker_url = os.environ.get('BROKER_URL')
broker_token = os.environ.get('BROKER_TOKEN')
pact_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"{}-{}.json".format(consumer,provider))
PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 5000
pact_base_url = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)
consumer_version="2.0.8"

def verify_add_articles_pact():
    """provider verifies pact contract files"""
    verifier = Verifier(provider='newsletterAutomation',
                        provider_base_url=pact_base_url)

    output, logs = verifier.verify_pacts(pact_file)
    assert (output == 0)

def verify_add_articles_pact_with_broker():
    """provider verifies pact contract files with Broker"""
    verifier = Verifier(provider='newsletterautomation',
                        provider_base_url=pact_base_url)

    default_opts = {
        'broker_url':broker_url,
        'broker_token':broker_token,
        'publish_version':'latest',
        'publish_verification_results':True,
        'consumer_version_selectors':[{"latest":True}]}
    output, logs = verifier.verify_with_broker(**default_opts)
    assert (output == 0)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v','--verify_method',type=str,default='broker',choices=['broker','pact'],help='enter if you want to verify pact file or pact file with broker')
    args = parser.parse_args()
    if args.verify_method == 'pact':
        verify_add_articles_pact()
    elif args.verify_method == 'broker':
        verify_add_articles_pact_with_broker()