from main import db

#All the Database Modles

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

class SNKRSList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	StoreName = db.Column(db.String(20), nullable=False)
	Brand = db.Column(db.String(20), nullable=False)
	Region = db.Column(db.String(20), nullable=False)
	Name = db.Column(db.String(20), nullable=False)
	StyleCode = db.Column(db.String(20), nullable=False)
	ColorWay = db.Column(db.String(20), nullable=False)
	LDate = db.Column(db.String(20), nullable=True)
	LTime = db.Column(db.String(20), nullable=True)
	Img = db.Column(db.String(20), nullable=False)
	Url = db.Column(db.String(20), nullable=False)
	Price = db.Column(db.Integer, nullable=False)
	Currency = db.Column(db.String(20), nullable=True)
	RestockWatch = db.Column(db.Boolen)

