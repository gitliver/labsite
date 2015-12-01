#!/usr/bin/env python

"""
    Lab Website
    ~~~~~~
    A first Flask + sqlite3 project - making a homepage for the lab,
    borrowing from Armin Ronacher's https://github.com/mitsuhiko/flask/tree/master/examples/flaskr
"""

import os
# from contextlib import closing
import sqlite3
import traceback
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, Blueprint, jsonify
from myapp import application
from myapp.forms.geneform import GeneForm 

motor = Blueprint('motor', __name__)

# --- db functions --- #
# sloppy violation of DRY principle - fix this later

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

@motor.route('/motor_neurons_tda')
def index():
    """motor neuron app built for Pablo - render a form in which a user can submit a gene"""
    form = GeneForm()

    return render_template('motor.html', form=form)

@motor.route('/_get_gene_result')
def get_result():
	"""JS AJAX calls this function, which queries the database based with a user-submitted gene"""

	# get the user-submitted gene
	mygene = request.args.get('mygene', "Not Found")
	mydb = request.args.get('mydb', "No database selected")

	# map the names of the db variable to table name
	mynamemap = {'db1': ('motor2304', '/static/motorimages/images_2304/'), 'db2': ('motor', '/static/motorimages/images_440/')}

	# genes that end with the 'Rik' string, have a different treatment
	if ('rik' == mygene[-3:].lower()): 
		mygene = mygene[:-3].upper() + 'Rik'
	# cast the case
	else:
		mygene = mygene[0].upper() + mygene[1:].lower()

	t=(mygene,)

	# this dict contains info about the gene
	geneinfo = {}

	# query gene in the database
	try:
		# set database 
		geneinfo['mydb'] = mydb

		# extract info from db
		cur = g.db.execute('select Gene, Cells, Mean, Min, Max, Connectivity, p_value, BH_p_value, Centroid, Dispersion, RNA_binding, Splicing, Surface, Transcription FROM ' + mynamemap[mydb][0] + ' WHERE Gene=?', t)
		x = cur.fetchone()
		geneinfo['Gene'] = x[0] 
		geneinfo['Cells'] = x[1] 
		geneinfo['Mean'] = x[2] 
		geneinfo['Min'] = x[3] 
		geneinfo['Max'] = x[4] 
		geneinfo['Connectivity'] = x[5] 
		geneinfo['p_value'] = x[6] 
		geneinfo['BH_p_value'] = x[7] 
		geneinfo['Centroid'] = x[8] 
		geneinfo['Dispersion'] = x[9] 
		geneinfo['RNA_binding'] = x[10]
		geneinfo['Splicing'] = x[11] 
		geneinfo['Surface'] = x[12] 
		geneinfo['Transcription'] = x[13]

		# get motor img path
		mopath = mynamemap[mydb][1] + geneinfo['Gene'][0] + '/' + geneinfo['Gene']
		# add img paths to geneinfo dict
		geneinfo['img1'] = mopath + "/output1.png"
		geneinfo['img2'] = mopath + "/output2.png"
		geneinfo['img3'] = mopath + "/output3.png"
		geneinfo['img4'] = mopath + "/output4.png"

	except:
		# if gene not in database, return this
		geneinfo = {
			'Gene': 'not found',
			'Cells': 'not found',
			'Mean': 'not found',
			'Min': 'not found',
			'Max': 'not found',
			'Connectivity': 'not found',
			'p_value': 'not found',
			'BH_p_value': 'not found',
			'Centroid': 'not found',
			'Dispersion': 'not found',
			'RNA_binding': 'not found',
			'Splicing': 'not found',
			'Surface': 'not found',
			'Transcription': 'not found',
			'img1': '/static/motorimages/notfound.480.jpg',
			'img2': '/static/motorimages/notfound.480.jpg',
			'img3': '/static/motorimages/notfound.480.jpg',
			'img4': '/static/motorimages/notfound.720.jpg'
		}

	# return jsonify(result=mygene)
	return jsonify(geneinfo)
