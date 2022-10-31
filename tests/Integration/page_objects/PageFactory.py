"""
PageFactory uses the factory design pattern.
get_page_object() returns the appropriate page object.
Add elif clauses as and when you implement new pages.
Pages implemented so far:
1. addarticles page
2. editarticles page
3. deletearticles page
"""
 

from page_objects.zero_page import Zero_Page
from page_objects.add_articles_page import Addarticles_Page
from page_objects.manage_articles_page import Managearticles_Page
from page_objects.edit_articles_page import Editarticles_Page
import conf.base_url_conf


class PageFactory():
    "PageFactory uses the factory design pattern."
    def get_page_object(page_name,base_url=conf.base_url_conf.base_url):
        "Return the appropriate page object based on page_name"
        test_obj = None
        page_name = page_name.lower()
        if page_name in ["zero","zero page","agent zero"]:
            test_obj = Zero_Page(base_url=base_url)
        elif page_name == "add articles page":
            test_obj =  Addarticles_Page(base_url=base_url)  
        elif page_name == "manage articles page":
            test_obj = Managearticles_Page(base_url=base_url)  
        elif page_name == "edit articles page":
            test_obj = Editarticles_Page(base_url=base_url)      
        return test_obj

    get_page_object = staticmethod(get_page_object)
