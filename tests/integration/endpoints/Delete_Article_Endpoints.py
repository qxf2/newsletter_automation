"""
API endpoints for article
"""
from bs4 import BeautifulSoup

class Delete_Article_Endpoints:
    "Class for article endpoints"

    def delete_articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/manage-articles'+suffix
        
    def delete_article(self,data,headers):
      "Adds a new article"
      url = self.delete_articles_url('')
      json_response = self.get(url,data=data,headers=headers)
      get_article = BeautifulSoup(json_response['text'], 'html.parser')
      first_article = (get_article.body.find_all('a',href=True,string='Delete',limit=1))
      for link in first_article:
        suffix = (link['href'])
      article_endpoint = self.base_url+suffix
      json_response = self.get(article_endpoint,data=data,headers=headers)
      return {
          'article_endpoint':article_endpoint,
          'response':json_response['text']
      }

   