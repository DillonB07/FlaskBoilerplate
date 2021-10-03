from flask import render_template, Blueprint

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/')
def home():
    return render_template('home.html', text='This route is in blueprints.py')