# tools/url_tool/__init__.py
from flask import Blueprint

url_tool_bp = Blueprint('url_tool', __name__, template_folder='templates', static_folder='static')

from . import routes