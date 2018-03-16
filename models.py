from main import db

#All the Database Modles

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	username = db.Column(db.String(80), unique=True, nullable=False)
# 	email = db.Column(db.String(120), unique=True, nullable=False)

class SNKRSList(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Site = db.Column(db.String(20), nullable=False)
	Brand = db.Column(db.String(20), nullable=False)
	Region = db.Column(db.String(20), nullable=False)
	Name = db.Column(db.String(20), nullable=False)
	StyleCode = db.Column(db.String(20), nullable=False)
	ColorWay = db.Column(db.String(20), nullable=False)
	LDate = db.Column(db.Date, nullable=True)
	LTime = db.Column(db.Time, nullable=True)
	Img = db.Column(db.String(200), nullable=False)
	Url = db.Column(db.String(200), nullable=False)
	Price = db.Column(db.Integer, nullable=False)
	Currency = db.Column(db.String(20), nullable=True)
	RestockWatch = db.Column(db.Boolean)

