"""
This script is used to send message to provided Skype channel
"""

import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import netlify_conf
from conf import skype_conf

def post_message_on_skype():
    """
    Posts a message on the set Skype channel
    """
    try:
        skype_message = f"""<b>Newsletter Automation - data validations outcome: </b> {netlify_conf.NETLIFY_URL}"""

        headers = {"Content-Type": "application/json"}
        payload = {
            "msg": skype_message,
            "channel": skype_conf.SKYPE_CHANNEL,
            "API_KEY": skype_conf.SKYPE_API_KEY,
        }
        response = requests.post(
            url=skype_conf.SKYPE_URL,
            json=payload,
            headers=headers,
        )

        if response.status_code == 200:
            print(f"Successfully sent the Skype message - {skype_message}")
        else:
            print("Failed to send Skype message!")
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print (error.response.text)
    except Exception as err:
        raise Exception(f"Unable to post message to Skype channel, due to {err}")

post_message_on_skype()
