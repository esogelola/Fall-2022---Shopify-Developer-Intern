from flask import Blueprint, render_template

blueprint = Blueprint('inventory', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')