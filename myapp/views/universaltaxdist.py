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
import matplotlib.pyplot as plt
import numpy as np
import StringIO
from myapp import application

universaltaxdist = Blueprint('universaltaxdist', __name__)

def myplot(x,y):
    """return a matplotlib figure object"""

    fig = plt.figure()
    z = plt.plot(x, y)
    return fig

# --- URL routing --- #

@universaltaxdist.route('/universaltaxdist')
def index():
    """universal taxonomic distributions app"""

    return render_template('universaltaxdist.html')

@universaltaxdist.route('/universaltaxdist/_generatefig')
def generatefig():
    """generate figure on the website without having to save an actual file on the server"""

    # just testing...
    x = np.arange(0,6,0.01)
    y = np.sin(x)
    f = myplot(x,y)
    img = StringIO.StringIO()
    f.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')
