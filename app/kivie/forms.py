from flask_wtf import Form
from wtforms import Field, StringField,BooleanField,SubmitField,IntegerField
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms.widgets import TextInput
from .models import Styles,Colors,Catalog

class TagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u', '.join(self.data)
        else:
            return u''

    def process_formdata(self,valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = []

class ExampleForm(Form):
    num = IntegerField()
    submit = SubmitField('POST')

