from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,request,current_app
from .. import db
from . import kivie

@kivie.route('/')
def index():
	return render_template('kivie/index.html')

