#!/usr/bin/env python

"""
    Lab Website
    ~~~~~~
    A first Flask + sqlite3 project - making a homepage for the lab,
    borrowing from Armin Ronacher's https://github.com/mitsuhiko/flask/tree/master/examples/flaskr
"""

# import os
# from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Blueprint
from myapp import application

motor = Blueprint('motor', __name__)

# --- db functions --- #
# slopping violation of DRY principle - fix this later

def connect_db():
    """Connects to the specific database."""
    return sqlite3.connect(application.config['DATABASE'])

@motor.before_request
def before_request():
    # without the try/except block, nginx will implode if there's an exception
    try:
        g.db = connect_db()
    except:
	print("Doh! Error connecting to db")

@motor.teardown_request
def teardown_request(exception):
    try:
        db = getattr(g, 'db', None)
        if db is not None:
            db.close()
    except:
        print("Doh! Error closing db")

# --- URL routing --- #

@motor.route('/motor_neurons')
def index():
    """motor neuron app built with Pablo"""
    # cur = g.db.execute('select iscurrent, name, title, bio, email, imagefile, webpage from people order by id')
    # return [dict(iscurrent=row[0], name=row[1], title=row[2], bio=row[3], email=row[4], imagefile=row[5], webpage=row[6]) for row in cur.fetchall()]
    return render_template('motor.html')
