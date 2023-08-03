"""
This module contains a test for the Newsletter Automation API.

The test validates the API's endpoint for retrieving articles ie. '/api/articles',
against the OpenAPI documentation.

It uses schemathesis and hypothesis libraries for test case generation and validation.
"""

import os
import schemathesis
from hypothesis import settings

schema = schemathesis.from_path("newsletter_api_spec.json", base_url="https://staging-newsletter-generator.qxf2.com")

@settings(max_examples=20)
@schema.parametrize(endpoint="/api/articles\\Z")
def test_newsletter_api(case):
    """
    Test the Newsletter API for retrieving articles.

    Args:
        case: Test case generated by schemathesis.
    """
    case.call_and_validate(headers={"x-api-key": os.environ.get("API_KEY")})
    