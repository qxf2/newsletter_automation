"""
Decorator for authenticating all pages
"""

from functools import wraps
from flask import render_template, session
from flask import Flask, request, jsonify
import conf.userlist_conf as conf

USER_LIST = conf.USER_LIST
                
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

    def requires_auth_api(app_func):
        "verify given user authentication details"
        @wraps(app_func)
        def decorated(*args, **kwargs):
            "Execute app_func only if authentication is valid"
            auth = request.authorization
            auth_flag = True

            if not auth:
                auth_flag = False
                return authenticate_error(auth_flag)
            elif not check_auth(auth.username, auth.password):
                return authenticate_error(auth_flag)
            return app_func(*args, **kwargs)

        return decorated

def check_auth(username, password):
    "check if the given is valid"
    user = [user for user in USER_LIST if user['name']
            == username and user['password'] == password]
    if len(user) == 1:
        return True
    return False


def authenticate_error(auth_flag):
    "set auth message based on the authentication check result"
    if auth_flag is True:
        message = {'message': "Authenticate with proper credentials"}
    else:
        message = {'message': "Require Basic Authentication"}
    response = jsonify(message)
    response.status_code = 401
    response.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return response