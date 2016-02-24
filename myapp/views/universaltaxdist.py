#!/usr/bin/env python

"""
    Universal Taxonomic Distributions App
    ~~~~~~
"""
import os
import sqlite3
import traceback
import subprocess
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Blueprint, jsonify, send_file
from flask_restful import Resource, Api
from myapp import application
from werkzeug import secure_filename
# import json

universaltaxdist = Blueprint('universaltaxdist', __name__)

api = Api(application)

# path to uploads
UPLOAD_FOLDER = os.getcwd() + '/labsite/uploads'
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# limit file size to 2M
application.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# http://flask-restful-cn.readthedocs.org/en/0.3.4/quickstart.html
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/universaltaxdist/helloworld')

class Qstat(Resource):
    def get(self, job_id):
        scripts = os.getcwd() + '/labsite/scripts'
	# for a given job id, return its state
	jobstate = subprocess.check_output('{}/getqstat.sh {}'.format(scripts, job_id), shell=True)
	return {'job_id': job_id, 'state': jobstate}

api.add_resource(Qstat, '/universaltaxdist/qstat/<string:job_id>')

class LsFiles(Resource):
    def get(self, job_id):
        scripts = os.getcwd() + '/labsite/scripts'
	# for a given job id, return '1' if files associated with that job have been created
	filesexist = subprocess.check_output('{}/lsfiles.sh {}'.format(scripts, job_id), shell=True)
	return {'job_id': job_id, 'files': filesexist}

api.add_resource(LsFiles, '/universaltaxdist/files/<string:job_id>')

# following: http://flask.pocoo.org/docs/0.10/patterns/fileuploads/

# check if file extension is okay
def allowed_file(filename):
    ALLOWED_EXTENSIONS = set(['txt', 'dat'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# check if file is properly formatted
def checkfile(filepath):
    pass

# --- URL routing --- #

@universaltaxdist.route('/universaltaxdist', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
	    filepath = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
	    # check file is legit
	    checkfile(filepath)

	    # scripts path
            scripts = os.getcwd() + '/labsite/scripts'
	    # qsub jobs on the cluster, return job id, file name
	    jid = subprocess.check_output('{}/dotreejob.sh {}'.format(scripts, filepath), shell=True)

            return redirect(url_for('.utax', jid = jid, filename = filename))

    return render_template('universaltaxdist.html')

@universaltaxdist.route('/universaltaxdist/res/<jid>/<filename>')
def utax(jid, filename):
    return render_template('universaltaxdistres.html', myjid = jid, myfile = filename)
