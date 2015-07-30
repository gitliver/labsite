#!/usr/bin/env python

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class GeneForm(Form):
	"""a form for submitting a gene name"""
	# after http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

	geneid = StringField('geneid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)
