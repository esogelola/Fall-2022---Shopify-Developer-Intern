from flask import Blueprint, render_template

blueprint = Blueprint('inventory', __name__)

@blueprint.route('/inventory')
def index():
    return render_template('inventory/index.html')

@blueprint.route('/product', methods = ['GET','POST'])
def product():
    return render_template('inventory/product.html')

@blueprint.route("/location", methods = ['GET', 'POST'])
def location():
    return render_template('inventory/location.html')

@blueprint.route("/transfers", methods = ['GET', 'POST'])
def transfers():
    return render_template('inventory/transfer.html')