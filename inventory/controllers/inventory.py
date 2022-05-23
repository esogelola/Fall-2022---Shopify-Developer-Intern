from flask import Blueprint, render_template, url_for, redirect, flash, request, jsonify

from inventory.models.inventory import Inventory
from inventory.models.product import Product
from inventory.models.location import Location
from inventory.models.transfer import Transfer


from inventory.extensions import db

blueprint = Blueprint('inventory', __name__)


@blueprint.route('/inventory')
def index():
    data_inventory = Inventory.query.all()
    has_inventory = bool(data_inventory)
    # TODO: Pass has_inventory to render to display warning message

    return render_template('inventory/index.html',
                           data_inventory=data_inventory,
                           has_inventory=has_inventory)


@blueprint.route('/product', methods=['GET', 'POST'])
def product():
    if (request.method == "POST") and ('product_name'
                                       in request.form) and ('product_qty'
                                                             in request.form):
        product_name = request.form["product_name"]
        product_qty = request.form["product_qty"]
                                                              
        print({product_name, product_qty})
        new_product = Product(product_name=product_name,
                              product_qty=product_qty)

        try:
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for("product"))

        except:
            products = Product.query.order_by(Product.product_id).all()
            return render_template("inventory/product.html", products=products)
    else:
        products = Product.query.order_by(Product.product_id).all()
        print(products)
        return render_template("inventory/product.html", products=products)

@blueprint.route("/update-product/<product_id>", methods=["POST"])
def updateProduct(product_id):
    product = Product.query.get_or_404(product_id)
    old_product = product
  
    product.product_name   = request.form['product_name']
    product.product_qty   = request.form['product_qty']

    
    try:
        
        update_transfer=  Transfer.query\
        .join(Product, Transfer.product_name == old_product.product_name)\
        .add_columns(
            Transfer.transfer_id,
            Transfer.product_qty,
            Product.product_name, 
            Transfer.transfer_from,
            Transfer.transfer_to,
            Transfer.transfer_time)\
        .all()
        print(update_transfer)
        for trans in update_transfer:
          trans.product_name = product.product_name
          trans.product_qty = product.product_qty
        db.session.commit()
        return redirect("/product")

    except:
        print("There was an issue while updating the Product")
        render_template("inventory/product.html", error="There was an issue while updating the Product")


@blueprint.route("/location", methods=['GET', 'POST'])
def location():
  if (request.method == "POST") and ('location_name' in request.form):
    location_name = request.form["location_name"]
    new_location = Location(location_name=location_name)

    try:
      db.session.add(new_location)
      db.session.commit()
      return redirect("/location")

    except:
      locations = Location.query.order_by(Location.location_id).all()
      return render_template("inventory/location.html", locations=locations)
  else:
    locations = Location.query.order_by(Location.location_id).all()
    return render_template("inventory/location.html", locations=locations)
      

@blueprint.route("/update-location/<location_id>", methods=["POST"])
def updateLocation(location_id):
    location = Location.query.get_or_404(location_id)
    old_location = location
  
    location.location_name   = request.form['location_name']

    
    try:
        db.session.commit() 
        # trans1 = Transfer.query.filter(Transfer.transfer_from == old_location.transfer_from).all()
        # trans2 = Transfer.query.filter(Transfer.transfer_to == old_location.transfer_to).all()    

        # for tra in trans1:
        #   tra.transfer_to = location.transfer_to
        # for tra in trans2:
        #   tra.transfer_to = location.transfer_to
        # db.session.commit()
        return redirect("/location")

    except:
        print("There was an issue while updating the Product")
        render_template("inventory/location.html", error="There was an issue while updating the Product")


@blueprint.route("/transfers", methods=['GET', 'POST'])
def transfers():
  if request.method == "POST" :
    product_name      = request.form["product_name"]
    qty             = request.form["product_qty"]
    transfer_from    = request.form["transfer_from"]
    transfer_to      = request.form["transfer_to"]
    
    if transfer_from != transfer_to and transfer_to != transfer_from:
      new_transfer = Transfer(product_name=product_name, product_qty=qty, transfer_from=transfer_from, transfer_to=transfer_to)
      new_inventory = Inventory(location=transfer_to, product_name=product_name, product_qty=qty)
      
      try:
        db.session.add(new_transfer)
        db.session.add(new_inventory)
        db.session.commit()
        return redirect("/transfers")
      except:
        return render_template('inventory/transfer.html', error="There Was an issue while adding a new Transfer")
    else:
      products    = Product.query.order_by(Product.product_id).all()
      locations   = Location.query.order_by(Location.location_id).all()
      transfers = Transfer.query\
        .join(Product, Transfer.product_name == Product.product_name)\
        .add_columns(
            Transfer.transfer_id,
            Transfer.product_qty,
            Product.product_name, 
            Transfer.transfer_from,
            Transfer.transfer_to,
            Transfer.transfer_time)\
        .all()
      return render_template("inventory/transfer.html", transfers=transfers, products=products, locations=locations,  error="There Was an issue while adding a new Transfer")
  else:
    products    = Product.query.order_by(Product.product_id).all()
    locations   = Location.query.order_by(Location.location_id).all()
    transfers = Transfer.query\
        .join(Product, Transfer.product_name == Product.product_name)\
        .add_columns(
            Transfer.transfer_id,
            Transfer.product_qty,
            Product.product_name, 
            Transfer.transfer_from,
            Transfer.transfer_to,
            Transfer.transfer_time)\
        .all()
    
    return render_template("inventory/transfer.html", transfers=transfers, products=products, locations=locations)



@blueprint.route("/delete-product/<product_id>")
def deleteProduct(product_id):
    product_to_delete = Product.query.get_or_404(product_id)

    try:
        db.session.delete(product_to_delete)
        db.session.commit()
        return redirect("/product")
    except:
        return "There was an issue while deleteing the Product"
      
@blueprint.route("/delete-location/<location_id>")
def deleteLocation(location_id):
    location_to_delete = Location.query.get_or_404(location_id)

    try:
        db.session.delete(location_to_delete)
        db.session.commit()
        return redirect("/location")
    except:
        return "There was an issue while deleteing the Product"