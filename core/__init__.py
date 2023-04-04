from flask import Flask
import os
from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate
from flaskext.markdown import  Markdown

from .extensions import db

load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    migrate = Migrate(app, db)
    markdown = Markdown(app)

    # register bp's
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # import models
    # from .models import MODEL_NAME

    @app.route('/test')
    def test():
        return 'test complete'

    return app

