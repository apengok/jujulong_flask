#-*- coding:UTF-8 -*-

from datetime import datetime
from flask import current_app,request,url_for
from .. import db

class Cloth:
    BRA=1
    PANTS=2

class Styles(db.Model):
    __tablename__ = 'styles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),unique=True)

    @staticmethod
    def insert_styles():
        styles=(u'呼吸',u'高端',u'烧花',u'樱花恋',u'冰绿',u'蜜粉',u'酒红',u'黛黑',u'藕色',u'豆绿',u'驼灰',u'幸运红',u'烟青蓝')
        for s in styles:
            style = Styles.query.filter_by(name=s).first()
            if style is None:
                style = Styles(name=s)
                db.session.add(style)
        db.session.commit()

    def repr(self):
        return '<Styles %r>'%self.style

class Colors(db.Model):
    __tablename__ = 'colors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(10),unique=True)
    style_id = db.Column(db.Integer,db.ForeignKey('styles.id'))
    catalog = db.relationship('Catalog',backref='color',lazy='dynamic')

    @staticmethod
    def insert_colors():
        colors={
                u'呼吸':(u'黑色',u'肤色',u'豹纹'),
                u'高端':(u'裸灰',u'裸色'),
                u'烧花':(u'中国红',u'富贵粉'),
                u'樱花恋':(u'典雅黑',u'幸福红',u'樱花粉'),
                u'冰绿':(u'冰绿',),
                u'蜜粉':(u'蜜粉',),
                u'酒红':(u'酒红',),
                u'黛黑':(u'黛黑',),
                u'藕色':(u'藕色',),
                u'豆绿':(u'豆绿',),
                u'驼灰':(u'驼灰',),
                u'幸运红':(u'幸运红',),
                u'烟青蓝':(u'烟青蓝',)
                }
        for s in colors:
            id_style = Styles.query.filter_by(name=s).first()
            for c in colors[s]:
                color = Colors.query.filter_by(name=c).first()
                if color is None:
                    color = Colors(name=c)
                    color.style_id = id_style.id
                    db.session.add(color)
        db.session.commit()

    def repr(self):
        return '<Color %r>'%self.name

class Catalog(db.Model):
    __tablename__ = 'catalog'
    id = db.Column(db.Integer,primary_key=True)
    cloth = db.Column(db.String(10))
    color_id = db.Column(db.Integer,db.ForeignKey('colors.id'))
    size = db.Column(db.String(10))
    totoal = db.Column(db.Integer)
    coming = db.Column(db.Integer)
    sale = db.Column(db.Integer)
    receved = db.Column(db.Integer)
    storge = db.Column(db.Integer)
    left = db.Column(db.Integer)
    diff = db.Column(db.Integer)


    def storge_json(self):
        json_cat = {
                self.cloth:{self.color.name:{self.size:{'storge':self.storge}}}
                }
        return json_cat


    @staticmethod
    def insert_catalog():
       catalogs = {
               u'内衣':
               {
                   u'黑色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'肤色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'豹纹':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'裸灰':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'裸色':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'中国红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'富贵粉':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'典雅黑':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'幸福红':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'樱花粉':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'冰绿':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   u'蜜粉':('70A','75A','80A','85A','70B ','75B','80B','85B','70C','75C','80C'),
                   u'酒红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   u'黛黑':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   },
               u'内裤':{
                   u'黑色':('M','L','XL'),
                   u'肤色':('M','L','XL'),
                   u'豹纹':('M','L','XL'),
                   u'裸灰':('M','L','XL'),
                   u'裸色':('M','L','XL'),
                   u'中国红':('M','L','XL'),
                   u'富贵粉':('M','L','XL'),
                   u'典雅黑':('M','L','XL','XXL'),
                   u'幸福红':('M','L','XL','XXL'),
                   u'樱花粉':('M','L','XL','XXL'),
                   u'冰绿':('M','L','XL'),
                   u'蜜粉':('M','L','XL'),
                   u'酒红':('M','L','XL'),
                   u'黛黑':('M','L','XL'),
                   u'藕色':('L','XL','XXL'),
                   u'豆绿':('L','XL','XXL'),
                   u'驼灰':('L','XL','XXL'),
                   u'幸运红':('L','XL','XXL'),
                   u'烟青蓝':('L','XL','XXL'),
                   }
               }
       for s in catalogs:
           for c in catalogs[s]:
               id_color = Colors.query.filter_by(name=c).first()
               if id_color is None:
                   print c
                   continue
               for p in catalogs[s][c]:
                   cat = Catalog(size=p)
                   cat.cloth = s
                   cat.color_id = id_color.id
                   db.session.add(cat)
       db.session.commit()

    def repr(self):
        return '<Style %r>'%self.size



