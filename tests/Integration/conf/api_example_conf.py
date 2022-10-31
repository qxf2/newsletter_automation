import time

# Setting current timestamp
current_timestamp =str(int(time.time()))

# Article details
article_url = 'https://www.tutorialspoint.com/software_testing_dictionary/accessibility_test.htm'
article_title = 'Automation Test Title'
article_description = 'Automation Test Description'
article_id = '2'
reading_time = '15'
article_editors = ['Arun','Raji','Avinash','Rahul','Akkul']

# base url
api_url = "http://127.0.0.1:5000"

# article details
article_details = {'url':'https://www.tutorialspoint.com/software_testing_dictionary/accessibility_test.htm'+current_timestamp,'title':'Software Automation Testing','description':'Automation Testing','time':'15','category_id':'3','article_editor':'Raji'}

# authentication details
headers = {'x_api_key':'Enter your APIkey'}




