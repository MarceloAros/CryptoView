from flask import Flask
from flask import render_template
#import csv
#import datetime
#import json
import requests
from config import DevelopmentConfig
from models import db

app = Flask(__name__)#nuevo objeto
#app.config.from_object(DevelopmentConfig)

@app.route('/')#rutas a entrar por el usuario
def index():
	return render_template('index.html')


if __name__ == '__main__':
	#app.init_app(app)  cargar configuraciones
	app.run()#ejecuta el servidor, actualiza los cambios (debug = True)
