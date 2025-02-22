from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_jwt_extended import JWTManager


db = SQLAlchemy()
jwt = JWTManager()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    from .controllers import api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    return app
