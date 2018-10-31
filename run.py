from flask import Flask
import requests
import xlrd
from serialnumber import Main
from spreadUpdate import Write

app = Flask(__name__)

@app.route("/<serialNumber>")
def serial(serialNumber):
	return	Main(serialNumber)

@app.route("/update")
def update():
	return Write()
	
if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080)	

