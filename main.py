from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from SNKRSScrapper import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data.db'
db = SQLAlchemy(app)

from models import *

@app.route('/', methods=['GET'])
def index():
	return 

@app.route('/comingUp', methods=['GET']) #UpComming Releases Calendar
def comingUp():
	return

@app.route('/restock', methods=['GET']) #Restock Watch
def restock():

	SNKRlist = SNKRSList.query.all()
	return render_template("Restock.html", list=SNKRlist)

@app.route('/releases', methods=['GET']) #Todays Releases
def releases():
	return

@app.route('/portfolio', methods=['GET']) # Portfolio of user Sneaker Collection
def portfolio():
	return

@app.route('/search', methods=['POST']) #Searching for shoes from websites
def search():
	StyleCode = request.form['ID']
	region = request.form['region']
	WS = request.form['website']

	return

@app.route('/add', methods=['POST'])  # Adding to the database
def add():
	StyleCode = request.form['ID']
	Region = request.form['region']
	Site = request.form['website']

	s = Shoe(Site, Region, StyleCode)
	shoe = SNKRSList(StoreName=s.StoreName,
						Brand=s.Brand,
						Region=s.Region,
						Name=s.Name,
						StyleCode=s.StyleCode,
						ColorWay=s.ColorWay,
						LDate=s.LDate,
						LTime=s.LTime,
						Img=s.Img,
						Url=s.Url,
						Price=s.Price,
						Currency=s.Currency,
						RestockWatch=False)
	db.session.add(shoe)
	db.session.commit()
	return


if __name__ == "__main__":
	app.run(debug=True)
