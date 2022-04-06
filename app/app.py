import os
from flask import Flask

from . import cards
from . import decks
from . import static_pages


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(cards.routes.blueprint)
    app.register_blueprint(decks.routes.blueprint)
    app.register_blueprint(static_pages.routes.blueprint)
