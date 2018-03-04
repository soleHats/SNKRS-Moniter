from flask import Flask, render_template, request
#from SneakerInfo import NikeShoe


app = Flask(__name__)

@app.route('/', methods=['GET'] )
def index():
	return render_template("Restock.html")

@app.route('/upload', methods=['POST'])
def prosess():
	return ""


if __name__ == "__main__":
	app.run()
