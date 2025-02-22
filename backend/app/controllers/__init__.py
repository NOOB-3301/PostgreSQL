from flask import Blueprint

api_bp = Blueprint('api', __name__)
blog_bp = Blueprint('blog', __name__)
from . import auth, user
from . import blogs
