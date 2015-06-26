#!/usr/bin/env python

from flask import Flask

# Following: http://flask.pocoo.org/docs/0.10/patterns/packages/
# 1. the Flask application object creation has to be in the __init__.py file. 
# That way each module can import it safely and the __name__ variable will resolve to the correct package.
# 2. all the view functions (the ones with a route() decorator on top) have to be imported in the __init__.py file. 
# Not the object itself, but the module it is in. Import the view module after the application object is created.

# create our application 
application = Flask(__name__)

# Load the configuration settings
application.config.from_object('myapp.default_settings')

import myapp.views
