"""
Decorator for authenticating all pages
"""

from functools import wraps
from flask import render_template, session, request, jsonify
import conf.apikey_conf as APIKEY

class Authentication_Required:
    "Authentication for all classes"
    def requires_auth(func):
        "verify given user authentication details"
        @wraps(func)
        def decorated(*args, **kwargs):
            "Execute func only if authentication is valid"
            try:
                current_user = session['logged_user']
                if current_user:
                    return func(*args, **kwargs)
            except Exception as e:
                return render_template("unauthorized.html")

        return decorated
    
    def requires_apikey(func):
        " Decorator function to require API Key "
        @wraps(func)
        def decorated(*args, **kwargs):
            " Decorator function that does the checking "
            if request.headers.get('x-api-key') and request.headers.get('X-API-KEY') == APIKEY.API_KEY:
                return func(*args, **kwargs)
            else:
                return authenticate_error(func)
        return decorated

def authenticate_error(auth_flag):
    "set authentication message "
    message = {'message': "API key is not valid"}
    response = jsonify(message)
    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return response