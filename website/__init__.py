from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import views
    from .blueprint import blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(blueprint, url_prefix='/blueprint')

    return app
