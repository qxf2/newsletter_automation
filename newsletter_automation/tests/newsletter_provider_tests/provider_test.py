""" provider verifies pact contracts """

import logging
import os,sys
from pact import Verifier
import pytest

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

PACT_FILE = "./articleslambda-newsletterautomation.json"
PACT_MOCK_HOST = 'localhost'
PACT_MOCK_PORT = 5000
PACT_BASE_URL = "http://{}:{}".format(PACT_MOCK_HOST, PACT_MOCK_PORT)

def test_add_articles():
    verifier = Verifier(provider='newsletterAutomation',
                        provider_base_url=PACT_BASE_URL)

    output, logs = verifier.verify_pacts(PACT_FILE)
    assert (output == 0)