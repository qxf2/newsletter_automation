import os
import time
import random

current_timestamp =str(int(time.time()))
subject = "99-Dec-1900"
opener = "From the simplest to the most complex application, automation is present in many forms in our everyday life. Common examples include household thermostats controlling boilers, the earliest automatic telephone switchboards, electronic navigation systems, or the most advanced algorithms behind self-driving cars."
preview = "From the simplest to the most complex application, automation is present in many forms in our everyday life. Common examples include household"

categories = ['pastweek','currentweek','automation corner','comic']
article_list_create_newsletter = []
for category in categories:
    article_list_create_newsletter.append({'URL':f'https://www.qxf2.com/{category}/'+current_timestamp, 'TITLE':f'A {category} article', 'DESCRIPTION':f'{category} advanced-python/python-mutable-and-immutable', 'RUNTIME':'10', 'CATEGORY':category})
       

