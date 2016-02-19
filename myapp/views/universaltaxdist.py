#!/usr/bin/env python

"""
    Universal Taxonomic Distributions App
    ~~~~~~
"""
import os
import sqlite3
import traceback
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Blueprint, jsonify, send_file
from myapp import application
from werkzeug import secure_filename

universaltaxdist = Blueprint('universaltaxdist', __name__)

# path to uploads
UPLOAD_FOLDER = os.getcwd() + '/labsite/uploads'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# limit file size to 2M
application.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# following: http://flask.pocoo.org/docs/0.10/patterns/fileuploads/

# check if file extension is okay
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# --- URL routing --- #

@universaltaxdist.route('/universaltaxdist', methods=['GET', 'POST'])
def upload_file():

    print('checkpoint 0') 

    if request.method == 'POST':
        print('checkpoint 1') 
        file = request.files['file']
        print('checkpoint 2') 
        if file and allowed_file(file.filename):
            print('checkpoint 3') 
            filename = secure_filename(file.filename)
            print('checkpoint 4') 
	    filepath = os.path.join(application.config['UPLOAD_FOLDER'], filename)
	    print('checkpoint path: ' + filepath) 
            file.save(filepath)
            print('checkpoint 5') 
            return redirect('/universaltaxdist/res')

    return render_template('universaltaxdist.html')

@universaltaxdist.route('/universaltaxdist/res')
def utax():
    return render_template('universaltaxdistres.html')
