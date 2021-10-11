""" when any changes to provider apis, provider needs to run contracts and check if its breaking any consumer
can verify contracts using pact verifier CLI >> pact-verifier --provider-base-url=http://localhost:port --pact-url=./contract.json
or using python pact verifier lib
"""

import logging
import os,sys
from pact import Verifier
import pytest
import pdb

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

provider = 'newsletterAutomation'
consumer = 'articlesLambda'
PACT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"{}-{}.json".format(consumer,provider))
PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 5000
PACT_BASE_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)
PACT_DIR = os.path.dirname(os.path.realpath(__file__))

def verify_add_articles_pact():
    """provider verifies pact contracts"""
    verifier = Verifier(provider='newsletterAutomation',
                        provider_base_url=PACT_BASE_URL)
    output, logs = verifier.verify_pacts(PACT_FILE)
    assert (output == 0)

if __name__ == '__main__':
    verify_add_articles_pact()