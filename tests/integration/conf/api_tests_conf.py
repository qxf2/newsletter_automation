import time
import os

# Setting current timestamp
current_timestamp =str(int(time.time()))

# Article details
article_url = 'https://www.qxf2.com/'
article_title = 'Automation Test Title'
article_description = 'Automation Test Description'
article_id = '1'
reading_time = '3'
article_editors = ['Arun','Raji','Avinash','Rahul','Akkul']

# article details
article_details = {'url':'https://www.qxf2.com/'+current_timestamp,'title':'Software Automation Testing','description':'Automation Testing','time':'15','category_id':'3','article_editor':'Raji'}

# authentication details
headers = {'x-api-key':os.environ.get('API_KEY','')}
