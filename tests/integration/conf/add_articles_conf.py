import time
import os
import random

email = os.environ.get('mail_id')
password = os.environ.get('password')
current_timestamp =str(int(time.time()))

categories = ['pastweek','currentweek','automation corner','comic']
article_list = []
for category in categories:
    article_list.append({'URL':f'https://www.qxf2.com/{category}/'+current_timestamp, 'TITLE':f'A {category}:'+str(random.randint(100000,999999)), 'DESCRIPTION':f'{category} advanced-python/python-mutable-and-immutable', 'RUNTIME':'10', 'CATEGORY':category})
