from flask import Blueprint

bp = Blueprint('flags', __name__)

from flags import routes