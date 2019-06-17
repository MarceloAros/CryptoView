from flask import Flask
from flask import render_template
import csv
import datetime
import json
import requests

app = Flask(__name__)#nuevo objeto

@app.route('/')#rutas a entrar por el usuario
def index():
	return render_template('index.html')


"""@app.route('/saluda')#rutas a entrar por el usuario
def saluda():
	return("hola mundo2")"""


if __name__ == '__main__':
	app.run(debug = False)#ejecuta el servidor, actualiza los cambios (debug = True)