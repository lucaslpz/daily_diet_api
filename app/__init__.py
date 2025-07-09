from flask import Flask
from .database import db
from .routes import bp as routes_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(routes_bp)

    return app