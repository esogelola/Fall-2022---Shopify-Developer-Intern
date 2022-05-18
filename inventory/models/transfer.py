from inventory.extensions import db
from datetime import datetime

class Transfer(db.Model):
  __tablename__ = 'transfer'
  transfer_id = db.Column(db.Integer, primary_key= True)
  transfer_time = db.Column(db.DateTime, default=datetime.utcnow)
  transfer_to = db.Column(db.String(35),nullable = False)
  transfer_from = db.Column(db.String(35),nullable = False)
  product_name = db.Column(db.String(35),nullable = False)
  product_qty = db.Column(db.Integer, nullable = False)
  def __repr__(self):
   return f"Movement('{self.transfer_id}','{self.transfer_time}','{self.transfer_from}','{self.transfer_to}','{self.product_name}','{self.product_qty}')"
  