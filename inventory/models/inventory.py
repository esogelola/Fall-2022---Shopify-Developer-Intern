from inventory.extensions import db
from datetime import datetime

class Inventory(db.Model):
  __tablename__ = 'inventory'
  inventory_id = db.Column(db.Integer, primary_key= True,nullable = False)
  location = db.Column(db.String(35),nullable = False)
  product_name = db.Column(db.String(35),nullable = False)
  product_qty = db.Column(db.Integer, nullable = False)
  
  def __repr__(self):
   return f"Inventory('{self.inventory_id}','{self.product_location}','{self.product_name}','{self.product_qty}')"
  