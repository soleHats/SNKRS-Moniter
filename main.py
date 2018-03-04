from flask import Flask, render_template, request
#from SneakerInfo import NikeShoe


app = Flask(__name__)

@app.route('/')
def index():
	return render_template("Restock.html")



if __name__ == "__main__":
	
	app.run()
