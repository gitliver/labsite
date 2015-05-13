#!/usr/bin/env python

from flask import Flask, render_template

application = Flask(__name__)
application.debug = True

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
