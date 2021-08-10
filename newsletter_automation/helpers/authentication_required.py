"""
Decorator for authenticating all pages
"""

from functools import wraps
from flask import render_template, session
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