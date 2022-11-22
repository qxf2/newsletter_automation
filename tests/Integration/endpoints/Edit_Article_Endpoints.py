"""
API endpoints for article
"""
from bs4 import BeautifulSoup

class Edit_Article_Endpoints:
    "Class for article endpoints"

    def edit_articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/manage-articles'+suffix
        
    def edit_article(self,data,headers):
      "Adds a new article"
      url = self.edit_articles_url('')
      json_response = self.get(url,data=data,headers=headers)
      get_article = BeautifulSoup(json_response['text'], 'html.parser')
      first_article = (get_article.body.find_all('a',href=True,string='Edit',limit=1))
      for link in first_article:
        suffix = (link['href'])
      article_endpoint = self.base_url+suffix
      json_response = self.get(article_endpoint,data=data,headers=headers)
      return {
          'article_endpoint':article_endpoint,
          'response':json_response['text']
      }
      
    def post_article(self,data,headers):
      "Adds a new article"
      url = self.edit_articles_url('')
      json_response = self.get(url,data=data,headers=headers)
      get_article = BeautifulSoup(json_response['text'], 'html.parser')
      first_article = (get_article.body.find_all('a',href=True,string='Edit',limit=1))
      for link in first_article:
        suffix = (link['href'])
      article_endpoint = self.base_url+suffix
      json_response = self.post(article_endpoint,data=data,headers=headers)
      return {
          'article_endpoint':article_endpoint,
          'response':json_response['text']
      }
    

   