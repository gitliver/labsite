#!/usr/bin/env python

import os

# configuration
# DATABASE = '/tmp/flaskr.db'
DATABASE=os.path.join(os.getcwd(), 'labsite/dbs/labsite.db')
# MOTORIMG =os.path.join(os.getcwd(), 'labsite/motorimages')
# Never leave debug mode activated in a production system, because it will allow users to execute code on the server!
WTF_CSRF_ENABLED = True
DEBUG = False
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
