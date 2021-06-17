"""
Helper for mailchimp actions

API references :
1. https://github.com/mailchimp/mailchimp-marketing-python
2. https://mailchimp.com/developer/marketing/guides/quick-start/

"""
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import conf.mailchimp_conf as conf_file

API_KEY=conf_file.MAILCHIMP_API_KEY
FROM_NAME = conf_file.FROM_NAME
REPLY_TO = conf_file.REPLY_TO
SERVER_PREFIX = conf_file.SERVER_PREFIX
SUBSCRIBER_LIST_ID = conf_file.SUBSCRIBER_LIST_ID
TEMPLATE_ID =conf_file.TEMPLATE_ID

class Mailchimp_Helper:
    def __init__(self):
        "Initialize mailchimp marketing api client"
        self.set_mailchimp_config()
        self.campaign_id = None
        
    def set_mailchimp_config(self):
        "set mailchimp connection config"
        self.client = MailchimpMarketing.Client()
        self.client.set_config({
            "api_key": API_KEY,
            "server": SERVER_PREFIX
        })
        
    def ping_mailchimp(self):
        "check mailchimp connection health"
        try:
            response = self.client.ping.get()
            return response
        except ApiClientError as error:
            return error.text
    
    def create_campaign(self,title,subject_line,preview_text):
        "creates campaign on mailchimp"
        try:
            response = self.client.campaigns.create({"type": "regular",
            "recipients":{"list_id":SUBSCRIBER_LIST_ID},
            "settings":
                {"subject_line":subject_line,
                "preview_text":preview_text,
                "title":title,
                "from_name":FROM_NAME,
                "reply_to":REPLY_TO,
                "template_id":TEMPLATE_ID
                }})
            self.campaign_id = response['id']
            return  self.campaign_id #campaign_id returned to be saved to db  
        except ApiClientError as error:
            return error.text
    
    def set_campaign_content(self):
        "sets the content text for the campaign"
        try:
            response = self.client.campaigns.set_content(self.campaign_id,{"template":{"id":TEMPLATE_ID,"sections":{}}})
            return response
        except ApiClientError as error:
            return error.text

    def schedule_campaign(self,schedule_time):
        "schedules a campaign to be delivered at a specified date"
        try:
            response = self.client.campaigns.schedule(self.campaign_id, {"schedule_time": schedule_time}) ##UTC time
            return response.status_code
        except ApiClientError as error:
            print(error.text)
            return error.text
    
    def send_test_email(self,test_emails=[]):
        "send campaign test email"
        try:
            response = self.client.campaigns.send_test_email(self.campaign_id, {"test_emails": test_emails, "send_type": "html"})
            return response.status_code
        except ApiClientError as error:
            return error.text

