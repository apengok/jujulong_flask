#-*- coding:UTF-8 -*-

from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,request,current_app
from .. import db
from . import kivie
from . models import Styles,Colors,Catalog
from . forms import ExampleForm

@kivie.route('/')
def index():
    page = request.args.get('page',1,type=int)
    pagination = Catalog.query.order_by(Catalog.color_id).paginate(page,
            per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    catalogs = pagination.items
    return render_template('kivie/index.html',catalogs=catalogs,pagination=pagination)

@kivie.route('/color_select/<color>')
def color_select(color):
    c = unicode(color)
    color_id = Colors.query.filter_by(name=c).first()
    catalogs = Catalog.query.filter_by(color_id=color_id.id)
    return render_template('kivie/index.html',catalogs=catalogs)

@kivie.route('/all')
def all_catalog():
    cats = Catalog.query.all()
    json_cats = {}
    for cat in cats:
        color = cat.color.name
        size = cat.size
        storge = cat.storge
        if color not in json_cats.keys():
            json_cats[color]={}
        json_cats[color][size] = storge

    return render_template('kivie/allcatalog.html',json_cats=json_cats)

@kivie.route('/edit',methods=['POST','GET'])
def edit():
    form = ExampleForm()
    #Sizes = current_app.config['KIVIE_CATALOGS'][u'内衣'.encode('utf-8')][u'黑色'.encode('utf-8')]
    Sizes = ('70A','75A','80A','85A')
    return render_template('kivie/edit.html',form=form,Sizes=Sizes)
