import obtencion_valores_nueva_Api2




obtencion_valores_nueva_Api2.app.run()













"""from flask import Flask, jsonify
from flask import render_template
import json
#import csv
#import datetime
#import json
import requests
#from config import DevelopmentConfig
#from models import db
#from models import User
#from obtencion_valores_nueva_Api import data2

app = Flask(__name__)#nuevo objeto
#app.config.from_object(DevelopmentConfig)
data2 = [
	{
		'BitcoinX': [],
		'BitcoinY': []
	},
	{
		'EthereumX': [],
		'EthereumY': []
	},
	{
		'RippleX': [],
		'RippleY': []
	},
	{
		'LitecoinX': [],
		'LitecoinY': []
	},
	{
		'Bitcoin_CashX': [],
		'Bitcoin_CashY': []
	},
	{
		'EOSX': [],
		'EOSY': []
	}
]

@app.route('/')#rutas a entrar por el usuario
def index():
	return render_template('index.html')

@app.route('/data')
def data():
        return jsonify(data2)
	

if __name__ == '__main__':
#	db.init_app(app)  #cargar configuraciones
#	with app.app_context():
#		db.create_all()
	app.run()#ejecuta el servidor, actualiza los cambios (debug = True)"""
