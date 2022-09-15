"""
This script is used to send message to provided Skype channel
"""

import os
import sys
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import skype_conf as config

with open("result.txt") as f:
    skype_message = f.read()


def post_message_on_skype(message):
    """
    Posts a message on the set Skype channel
    :param message: text
    """

    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "msg": message,
            "channel": config.SKYPE_CHANNEL,
            "API_KEY": config.SKYPE_API_KEY,
        }

        response = requests.post(
            url=config.SKYPE_URL,
            json=payload,
            headers=headers,
        )
        if response.status_code == 200:
            print(f"Successfully sent the Skype message - {message}")
        else:
            print("Failed to send Skype message", level="error")
    except Exception as err:
        raise Exception(f"Unable to post message to Skype channel, due to {err}")


post_message_on_skype(skype_message)
