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

    def insert_styles():
        styles=('呼吸','高端','烧花','樱花恋','冰绿','蜜粉','酒红','黛黑','藕色','豆绿','驼灰','幸运红','烟青蓝')
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

    def insert_colors():
        colors={
                '呼吸':('黑色','肤色','豹纹'),
                '高端':('裸灰','裸色'),
                '烧花':('中国红','富贵粉'),
                '樱花恋':('典雅黑','幸福红','樱花粉'),
                '冰绿':('冰绿',),
                '蜜粉':('蜜粉',),
                '酒红':('酒红',),
                '黛黑':('黛黑',),
                '藕色':('藕色',),
                '豆绿':('豆绿',),
                '驼灰':('驼灰',),
                '幸运红':('幸运红',),
                '烟青蓝':('烟青蓝',)
                }
        for s in colors:
            id_style = Styles.query.filter_by(name=s).first()
            for c in colors[s]:
                color = Colors.query.filter_by(name=c).first()
                if color is None:
                    color = Colors(name=c)
                    color.style_id = id_style
                    db.session.add(color)
        db.session.commit()

    def repr(self):
        return '<Color %r>'%self.name

class Catalog(db.Model):
    __tablename__ = 'catalog'
    id = db.Column(db.Integer,primary_key=True)
    cloth = db.Column(db.String(10))
    color_id = db.Column(db.Integer,db.ForeignKey('colors.id'))
    size = db.Colunmn(db.String(10))
    totoal = db.Column(db.Integer)
    coming = db.Column(db.Integer)
    sale = db.Column(db.Integer)
    receved = db.Column(db.Integer)
    storge = db.Column(db.Integer)
    left = db.Column(db.Integer)
    diff = db.Column(db.Integer)


    def insert_catalog():
       catalogs = {
               '内衣':
               {
                   '黑色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   '肤色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   '豹纹':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   '裸灰':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   '裸色':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   '中国红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   '富贵粉':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   '典雅黑':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   '幸福红':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   '樱花粉':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   '冰绿':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   '蜜粉':('70A','75A','80A','85A','70B ','75B','80B','85B','70C','75C','80C'),
                   '酒红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   '黛黑':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   },
               '内裤':{
                   '黑色':('M','L','XL'),
                   '肤色':('M','L','XL'),
                   '豹纹':('M','L','XL'),
                   '裸灰色':('M','L','XL'),
                   '裸色':('M','L','XL'),
                   '中国红':('M','L','XL'),
                   '富贵粉':('M','L','XL'),
                   '典雅黑':('M','L','XL','XXL'),
                   '幸福红':('M','L','XL','XXL'),
                   '樱花粉':('M','L','XL','XXL'),
                   '冰绿':('M','L','XL'),
                   '蜜粉':('M','L','XL'),
                   '酒红':('M','L','XL'),
                   '黛黑':('M','L','XL'),
                   '藕色':('L','XL','XXL'),
                   '豆绿':('L','XL','XXL'),
                   '驼灰':('L','XL','XXL'),
                   '幸运红':('L','XL','XXL'),
                   '烟青蓝':('L','XL','XXL'),
                   }
               }
       for s in catalogs:
           for c in catalogs[s]:
               id_color = Colors.query.filter_by(name=c).first()
               for p in catalogs[s][c]:
                   cat = Catalogs(size=p)
                   cat.cloth = s
                   cat.color_id = id_color
                   db.session.add(cat)
        db.session.commit()

    def repr(self):
        return '<Style %r>'%self.size



