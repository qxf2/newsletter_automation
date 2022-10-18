"""
Flask App for Newsletter automation
"""

from newsletter import app
import logging
import os

@app.before_first_request
def before_first_request():
    log_level = logging.INFO

    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)

    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    log_file = os.path.join(logdir, 'app.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s under method %(funcName)s: %(message)s'))
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

if __name__ == '__main__':
    print("running")
    app.run(debug=True)
