"""
API endpoints for article
"""

class Article_API_Endpoints:
    "Class for article endpoints"

    def articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/api'+suffix
        
    def add_article(self,data,headers):
      "Adds a new article"
      url = self.articles_url('/articles')
      json_response = self.post(url,data=data,headers=headers)
      print("json response is", json_response)
      return {
          'url':url,
          'response':json_response['json_response']
      }
