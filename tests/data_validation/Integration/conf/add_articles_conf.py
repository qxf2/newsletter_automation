import time

email  = "aruul.bhagkya@qxf2.com"
password = "AganSarwin@2021"
current_timestamp =str(int(time.time()))
article1 = {'URL':'https://www.python.org/downloads/'+current_timestamp,'TITLE':'postman api tool','DESCRIPTION':'tool which is used to get,post,put and delete request','RUNTIME':'10','CATEGORY':'pastweek'}
article2 = {'URL':'https://www.techbeamers.com/handle-alert-popup-selenium-python/'+current_timestamp,'TITLE':'handle-alert-popup-selenium','DESCRIPTION':'handle-alert-popup-selenium','RUNTIME':'15','CATEGORY':'currentweek'}
article3 = {'URL':'https://www.pythontutorial.net/advanced-python/python-mutable-and-immutable/'+current_timestamp,'TITLE':'advanced-python/python-mutable-and-immutable','DESCRIPTION':'advanced-python/python-mutable-and-immutable','RUNTIME':'5','CATEGORY':'automation corner'}
article4 = {'URL':'https://www.browserstack.com/guide/alerts-and-popups-in-selenium'+current_timestamp,'TITLE':'alerts-and-popups-in-selenium','DESCRIPTION':'alerts-and-popups-in-selenium','RUNTIME':'7','CATEGORY':'comic'}
article5 = {'URL':'https://www.pythontutorial.net/python-basics/python-numbers/'+current_timestamp,'TITLE':'python-basics/python-numbers','DESCRIPTION':'python-basics/python-numbers','RUNTIME':'5','CATEGORY':'uncategorized'}
article_list = [article1,article2,article3,article4,article5]