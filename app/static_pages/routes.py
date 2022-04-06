from flask import Flask, Blueprint, render_template

blueprint = Blueprint('/', __name__)


@blueprint.route('/')
def home():
    return render_template('home.html')
