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
from datetime import date
from myapp import application

# print statements will show up in the uWSGI logs
# print("debug")
# print(DATABASE)

# --- db functions --- #

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

def get_people():
    """get people entries from the db"""
    cur = g.db.execute('select iscurrent, name, title, bio, email, imagefile, webpage from people order by id')
    return [dict(iscurrent=row[0], name=row[1], title=row[2], bio=row[3], email=row[4], imagefile=row[5], webpage=row[6]) for row in cur.fetchall()]

def get_pubs():
    """get publication entries from the db"""
    cur = g.db.execute('select id, year, title, authors, journal, journal2, doi, doi2, journal_url, journal_url2, notes, ishightlight from publications order by id')
    return [dict(id=row[0], year=row[1], title=row[2], authors=row[3], journal=row[4], journal2=row[5], doi=row[6], doi2=row[7], journal_url=row[8], journal_url2=row[9], notes=row[10], highlight=row[11]) for row in cur.fetchall()]

def get_press():
    """get press entries from the db"""
    cur = g.db.execute('select id, year, mytext, journal_url from press order by id')
    return [dict(id=row[0], year=row[1], mytext=row[2], journal_url=row[3]) for row in cur.fetchall()]

# --- URL routing --- #

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/publications/')
@application.route('/publications/<int:myyear>')
def pubs(myyear=0):
    # db query
    entries = get_pubs()

    # default template is publications.html
    mytemplate='publications.html'

    # initialize 
    entries_year = []

    # if a year in the appropriate range is supplied
    if (myyear >= 1999 and myyear <= date.today().year):
        # entries_year is a list of entry dicts for a specific year
        entries_year = filter(lambda y: y['year'] == myyear, entries)
	# use a different template (a little bit of a DRY violation but oh well)
        mytemplate='publications_by_year.html'
    # else get complete publication list for all years
    else:
        # entries_year is a list of lists of entry dicts, segregated by year
        for i in reversed(range(1999,date.today().year + 1)):
            entries_year.append(filter(lambda y: y['year'] == i, entries))

    try:
        return render_template(mytemplate, mydata=entries_year, myyear=myyear)
    except:
        return render_template('error.html')

@application.route('/press')
def press():
    # db query
    entries = get_press()

    try:
        return render_template('press.html', mydata=entries)
    except:
        return render_template('error.html')

@application.route('/people')
@application.route('/people/<mystatus>')
def people(mystatus=None):
    entries = get_people()
    # data struct is a big list of entry dicts which looks something like this:
    # entries = [{'imagefile': u'raul.jpg', 'name': u'Raul Rabadan', 'iscurrent': 1, 'title': u'Principal Investigator', 'webpage': u'-', 'email': u'rabadan@dbmi.columbia.edu'}, {'imagefile': u'hossein.jpg', 'name': u'Hossein Khiabanian', 'iscurrent': 1, 'title': u'Associate Research Scientists', 'webpage': u'-', 'email': u'hossein@c2b2.columbia.edu'}, {'imagefile': u'jiguang.gif', 'name': u'Jiguang Wang', 'iscurrent': 1, 'title': u'Associate Research Scientists', 'webpage': u'-', 'email': u'-'}, {'imagefile': u'franny.png', 'name': u'Francesco Abate', 'iscurrent': 1, 'title': u'Postdoctoral Researchers', 'webpage': u'-', 'email': u'-'}]

    # list of lists of people dicts, segregated by title
    entries_title = []

    # titles of current members
    titles = ["Principal Investigator", "Associate Research Scientists", "Postdoctoral Researchers", "Doctoral Students", "Staff", "Master's Students", "Undergraduates", "Interns"]
    # titles of alumni
    if (mystatus == "alum"):
        titles = ["Alumni"]

    # make data struct 
    for i in titles:
	# if nonempty (i.e., there are members with the title)
	if (filter(lambda y: y['title'] == i, entries)):
            entries_title.append(filter(lambda y: y['title'] == i, entries))

    try:
        return render_template('people.html', mydata=entries_title, mystatus=mystatus)
    except:
        return render_template('error.html')

@application.route('/courses')
def courses():
    return render_template('courses.html')

@application.route('/research')
def research():
    return render_template('research.html')

@application.route('/researchstatement')
def researchstatement():
    return render_template('researchstatement.html')

@application.route('/software')
def softw():
    return render_template('software.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

@application.route('/raegyptiacus')
def bat():
    return render_template('raegyptiacus.html')
