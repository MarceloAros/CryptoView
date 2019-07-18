from flask import Flask
from flask import render_template
#import csv
#import datetime
#import json
import requests
#from config import DevelopmentConfig
#from models import db
#from models import User

app = Flask(__name__)#nuevo objeto
#app.config.from_object(DevelopmentConfig)

@app.route('/')#rutas a entrar por el usuario
def index():
	return render_template('index.html')


if __name__ == '__main__':
#	db.init_app(app)  #cargar configuraciones
#	with app.app_context():
#		db.create_all()
	app.run()#ejecuta el servidor, actualiza los cambios (debug = True)
