from flask import Blueprint

hello = Blueprint('hello', __name__)

from . import routes
