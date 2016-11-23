from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,request,current_app
from .. import db
from . import kivie
from . models import Styles,Colors,Catalog

@kivie.route('/')
def index():
    page = request.args.get('page',1,type=int)
    pagination = Catalog.query.order_by(Catalog.color_id).paginate(page,
            per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    catalogs = pagination.items
    return render_template('kivie/index.html',catalogs=catalogs,pagination=pagination)

