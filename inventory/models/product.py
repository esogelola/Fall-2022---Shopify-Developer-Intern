from inventory.extensions import db

class Product(db.Model):
  __tablename__ = 'product'
  product_id = db.Column(db.Integer, primary_key= True)
  product_name = db.Column(db.String(35), nullable = False)
  product_name = db.Column(db.String(35),unique = True ,nullable = False)
  product_qty = db.Column(db.Integer, nullable = False)
  def __repr__(self):
      return f"Product('{self.product_id}','{self.product_name}','{self.product_qty}')"
  