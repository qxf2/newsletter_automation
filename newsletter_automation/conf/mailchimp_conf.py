"""
Configuration for mailchimp integrtaion
"""
import os
MAILCHIMP_API_KEY = os.environ.get('MAILCHIMP_API_KEY')
SERVER_PREFIX = os.environ.get('SERVER_PREFIX')
SUBSCRIBER_LIST_ID = os.environ.get('SUBSCRIBER_LIST_ID')
FROM_NAME= 'Qxf2 Services'
REPLY_TO='informedtester@qxf2.com'