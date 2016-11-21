from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,request,current_app
from .. import db
from . import kivie

@kivie.route('/')
def catalogs():
	return render_template('kivie.html')

