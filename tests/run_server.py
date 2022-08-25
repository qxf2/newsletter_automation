"""
This module wraps around http.server.
It is useful in testing your changes to the website locally.

Source: https://stackoverflow.com/questions/10607621/a-simple-website-with-python-using-http.server-and-socketserver-how-to-onl
"""

import http.server
import socketserver

class Qxf2RequestHandler(http.server.SimpleHTTPRequestHandler):
    "A class to extend http.server"
    def do_GET(self):
        "Add .html if the page does not end with .html"
        if self.path[-5:]!='.html' and '.' not in self.path and self.path != '/':
            self.path += '.html'
        print ('Visiting the URL: ',self.path)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

#----START OF SCRIPT
if __name__=='__main__':
    Handler = Qxf2RequestHandler
    server = socketserver.TCPServer(('0.0.0.0', 6464),Handler)
    print ("Started the server on port 6464")
    server.serve_forever()