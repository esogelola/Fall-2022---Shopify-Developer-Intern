from inventory.extensions import db

class Location(db.Model):
  __tablename__ = 'location'
  location_id = db.Column(db.Integer, primary_key= True)
  location_name = db.Column(db.String(35),unique = True, nullable = False)
  def __repr__(self):
    return f"Location('{self.location_id}','{self.location_name}')"
    return "Location('{self.location_id}','{self.location_name}')"
  