from flask import Blueprint

kivie = Blueprint('kivie',__name__)

from . import views
