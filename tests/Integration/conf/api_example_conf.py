import time

# current timestamp
current_timestamp =str(int(time.time()))

# article details
article_url = 'https://www.tutorialspoint.com/software_testing_dictionary/accessibility_test.htm'
article_title = 'Test Title'
article_description = 'Test Description'
article_editors = ['Arun','Raji','Avinash','Rahul','Akkul']

# url
api_url = "http://127.0.0.1:5000"

# add article
article_details = {'url':'https://www.tutorialspoint.com/software_testing_dictionary/accessibility_test.htm'+current_timestamp,'title':'Testing','description':'Automation','category_id':'3','article_editor':'Raji'}

# authentication details
headers = {'x_api_key':'set your apikey'}


