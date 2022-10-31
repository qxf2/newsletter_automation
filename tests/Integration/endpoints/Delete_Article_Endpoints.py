"""
API endpoints for article
"""

class Delete_Article_Endpoints:
    "Class for article endpoints"

    def delete_articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/delete'+suffix
        
    def delete_article(self,data,headers):
      "Adds a new article"
      url = self.delete_articles_url('/262')
      json_response = self.get(url,data=data,headers=headers)
      return {
          'url':url,
          'response':json_response['json_response']
      }

   