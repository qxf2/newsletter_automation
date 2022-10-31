"""
API endpoints for article
"""

class Edit_Article_Endpoints:
    "Class for article endpoints"

    def edit_articles_url(self,suffix=''):
        """Append API end point to base URL"""
        return self.base_url+'/edit'+suffix

    def edit_article(self,data,headers):
      "Adds a new article"
      url = self.edit_articles_url('/261')
      json_response = self.get(url,data=data,headers=headers)
      #print('url in edit endpoint', json_response)
      return {
          'url':url,
          'response':json_response['text']
      }
         
    def post_article(self,data,headers):
      "Adds a new article"
      url = self.edit_articles_url('/261')
      json_response = self.post(url,data=data,headers=headers)
      #print('url in edit endpoint', json_response)
      return {
          'url':url,
          'response':json_response['text']
      }
    

   
