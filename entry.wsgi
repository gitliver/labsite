#!/usr/bin/env python

"""
    Lab Website
    ~~~~~~
    A first Flask + sqlite3 project - making a homepage for the lab,
    borrowing from Armin Ronacher's https://github.com/mitsuhiko/flask/tree/master/examples/flaskr
"""

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from contextlib import closing

# configuration
# DATABASE = '/tmp/flaskr.db'
DATABASE=os.path.join(os.getcwd(), 'labsite/dbs/labsite.db')
# Never leave debug mode activated in a production system, because it will allow users to execute code on the server!
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# print statements will show up in the uWSGI logs
# print("debug")
# print(DATABASE)

# create our application
application = Flask(__name__)
application.config.from_object(__name__)
# if set an environment variable called FLASKR_SETTINGS to specify a config file 
# to be loaded which will then override the default values
# application.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(application.config['DATABASE'])

@application.before_request
def before_request():
    # without the try/except block, nginx will implode if there's an exception
    try:
        g.db = connect_db()
    except:
	print("Doh! Error connecting to db")

@application.teardown_request
def teardown_request(exception):
    try:
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()
    except:
        print("Doh! Error closing db")

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/publications')
def pubs():
    return render_template('publications.html')

@application.route('/press')
def press():
    return render_template('press.html')

@application.route('/people')
def people():
    return render_template('people.html')

@application.route('/alumni')
def alum():
    return render_template('alumni.html')

@application.route('/formembers')
def formembers():
    return render_template('formembers.html')

@application.route('/courses')
def courses():
    return render_template('courses.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    application.run()
