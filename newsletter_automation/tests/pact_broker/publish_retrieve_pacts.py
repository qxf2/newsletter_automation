""" publish pacts to broker / retrieve pacts from broker"""

import requests
import json
import os,sys
import pdb

provider_val = 'newsletterautomation'
consumer_val = 'articleslambda'
broker_url = os.environ.get('PACT_BROKER')
broker_token = os.environ.get('BROKER_TOKEN')
pact_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"{}-{}.json".format(consumer_val,provider_val))
consumer_version="2.0.8"

def publish_to_broker():
    "publish the generated contract file to broker"
    if os.path.exists(pact_file):
        f = open(pact_file)
        PACT_DATA = json.load(f)
    else:
        print("pact file to be published is not found")
    url = '{}/pacts/provider/{}/consumer/{}/version/{}'.format(broker_url,provider_val,consumer_val,consumer_version)
    headers={'Content-type':'application/json','Authorization': 'Bearer {}'.format(broker_token)}
    response = requests.put(url,data=json.dumps(PACT_DATA),headers=headers)
    if response.status_code in (200,201):
        print("published the contract to broker successfully")
    else:
        print("error:{}".format(response.status_code))

def retrieve_pact_from_broker():
    "retrieve the published contract file from broker"
    url = '{}/pacts/provider/{}/consumer/{}/latest'.format(broker_url,provider_val,consumer_val)
    headers = {'Content-type':'application/json','Authorization': 'Bearer THdUg_ZEsgKWrV6_Yjc_Jw'}
    response = requests.get(url,headers=headers)

    print(f'Here is the pact: {response.text}')

if __name__ == "__main__":
    print(".....................Publishing the pact to Broker....................")
    publish_to_broker()
    print(".....................Retrieving the pact from Broker...................")
    retrieve_pact_from_broker()