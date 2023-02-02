"""
API endpoints for article
"""
import requests

class Delete_Article_Endpoints:
    "Class for article endpoints"

    def delete_articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/api/articles/all'+suffix
    
    def delete_article_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+''+suffix
    
    def delete_article(self,data,headers):
      "delete an article"
      url = self.delete_articles_url('')
      json_responses = self.get(url,data=data,headers=headers)
      all_articles = json_responses.get("json_response")
      for last_article in reversed(all_articles):
        all_articles_id = (last_article.get('article_id',None))
        endpoint = str(all_articles_id)
        break
      url = self.delete_article_url('/api/article/')+endpoint
      json_response = self.delete(url,data=data,headers=headers)
      return {
          'url':url,
          'response':json_response['json_response']
      }
   