#-*- coding:UTF-8 -*-

import unittest
import time
from datetime import datetime
from app import create_app,db
from app.kivie.models import Styles,Colors,Catalog


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Styles.insert_styles()
        Colors.insert_colors()
        Catalog.insert_catalog()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_style(self):
        s = Styles.query.filter_by(name=u'呼吸').first()
        self.assertTrue(u'呼吸' in s)
