from flask import Blueprint

bp = Blueprint('help', __name__)

from help import routes