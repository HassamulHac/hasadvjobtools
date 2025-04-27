# tools/json_to_csv/__init__.py
from flask import Blueprint

json_to_csv_bp = Blueprint('json_to_csv', __name__, template_folder='templates', static_folder='static')

from . import routes