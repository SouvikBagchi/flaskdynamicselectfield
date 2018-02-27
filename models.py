#THIS CONTAINS THE SQLALCHEMY ORM MODEL TO CONNECT TO THE DATABASE
from flask_app import db, app

class SelectTable(db.Model):

	__tablename__ = "selectTable"
	
	id = db.Column(db.Integer, primary_key = True)
	names = db.Column(String(20))
	
db.create_all()