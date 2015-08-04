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

# this is using the wtforms machinery and a full page refresh
# switch instead to AJAX call (see below)
if 0:
	@motor.route('/motor_neurons', methods=['GET', 'POST'])
	def index():
	    """motor neuron app built for Pablo"""
	    form = GeneForm()
	    if form.validate_on_submit():
		t=(form.geneid.data,)
		try:
			# extract info from db
			cur = g.db.execute('select Gene, Cells, Mean, Min, Max, Connectivity, p_value, BH_p_value, Centroid, Dispersion, RNA_binding, Splicing, Surface, Transcription FROM motor WHERE Gene=?', t)
			x = cur.fetchone()
			geneinfo = {'Gene': x[0], 'Cells': x[1], 'Mean': x[2], 'Min': x[3], 'Max': x[4], 'Connectivity': x[5], 'p_value': x[6], 'BH_p_value': x[7], 'Centroid': x[8], 'Dispersion': x[9], 'RNA_binding': x[10], 'Splicing': x[11], 'Surface': x[12], 'Transcription': x[13]}

			# get motor img path
			mopath = '/static/motorimages/' + str(form.geneid.data)[0] + '/' + str(form.geneid.data)

			return render_template('motorout.html', geneinfo=geneinfo, mopath=mopath, tmp='asdf')
		except:
			return render_template('error2.html')

	    return render_template('motor.html', form=form)

@motor.route('/motor_neurons', methods=['GET', 'POST'])
def index():
    """motor neuron app built for Pablo"""
    form = GeneForm()

    return render_template('motor.html', form=form)

@motor.route('/_get_gene_result')
def get_result():
	mygene = request.args.get('mygene', "Not Found")
	t=(mygene,)
	geneinfo = {}
	try:
		# extract info from db
		cur = g.db.execute('select Gene, Cells, Mean, Min, Max, Connectivity, p_value, BH_p_value, Centroid, Dispersion, RNA_binding, Splicing, Surface, Transcription FROM motor WHERE Gene=?', t)
		x = cur.fetchone()
		geneinfo = {
			'Gene': x[0], 
			'Cells': x[1], 
			'Mean': x[2], 
			'Min': x[3], 
			'Max': x[4], 
			'Connectivity': x[5], 
			'p_value': x[6], 
			'BH_p_value': x[7], 
			'Centroid': x[8], 
			'Dispersion': x[9], 
			'RNA_binding': x[10],
			'Splicing': x[11], 
			'Surface': x[12], 
			'Transcription': x[13]
		}

		# get motor img path
		mopath = '/static/motorimages/' + geneinfo['Gene'][0] + '/' + geneinfo['Gene']
		# add img paths to geneinfo dict
		geneinfo['img1'] = mopath + "/output1.jpg"
		geneinfo['img2'] = mopath + "/output2.jpg"
		geneinfo['img3'] = mopath + "/output3.jpg"
		geneinfo['img4'] = mopath + "/output4.jpg"

	except:
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

# example from http://flask.pocoo.org/docs/0.10/patterns/jquery/
@motor.route('/_add_numbers')
def add_numbers():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result=a + b)
