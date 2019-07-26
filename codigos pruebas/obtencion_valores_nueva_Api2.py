#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask import render_template
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import models
import main

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
	'start':'1',
	'limit':'100',
}
headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '0daaaa79-fa83-438b-a42b-f848e3e39421',
}
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

app = Flask(__name__)

@app.route('/')#rutas a entrar por el usuario
def index():
	return render_template('index.html')

@app.route('/data')
def data():
        return jsonify(data2)



def limpiar_datos(datos):
	if len(datos[0]['BitcoinX']) > 5 :
		data2[0]['BitcoinX'].pop(0)
		data2[0]['BitcoinY'].pop(0)
		data2[1]['EthereumX'].pop(0)
		data2[1]['EthereumY'].pop(0)
		data2[2]['RippleX'].pop(0)
		data2[2]['RippleY'].pop(0)
		data2[3]['LitecoinX'].pop(0)
		data2[3]['LitecoinY'].pop(0)
		data2[4]['Bitcoin_CashX'].pop(0)
		data2[4]['Bitcoin_CashY'].pop(0)
		data2[5]['EOSX'].pop(0)
		data2[5]['EOSY'].pop(0)

def insertar_datos(precio1, Ultima_actualizacion1,ausiliar):
	if ausiliar == 0:
		data2[0]['BitcoinX'].append(precio1)
		data2[0]['BitcoinY'].append(Ultima_actualizacion1)
	elif ausiliar == 1:
		data2[1]['EthereumX'].append(precio1)
		data2[1]['EthereumY'].append(Ultima_actualizacion1)
	elif ausiliar == 2:
		data2[2]['RippleX'].append(precio1)
		data2[2]['RippleY'].append(Ultima_actualizacion1)
	elif ausiliar == 3:
		data2[3]['LitecoinX'].append(precio1)
		data2[3]['LitecoinY'].append(Ultima_actualizacion1)
	elif ausiliar == 4:
		data2[4]['Bitcoin_CashX'].append(precio1)
		data2[4]['Bitcoin_CashY'].append(Ultima_actualizacion1)
	elif ausiliar == 6:
		data2[5]['EOSX'].append(precio1)
		data2[5]['EOSY'].append(Ultima_actualizacion1)

"""def Escribir_datos(data):
        dest=open("data.txt","w")
        for com in data:
                for i, p in com.items():
                        dest.write("%s "+":"+"%s \n" %(i, p))
        dest.close()"""

def obtenerValor():
	session = Session()
	session.headers.update(headers)

	try:
			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			#print (json.dumps(data,indent=4))
			#insertar valor en tablas
			ausiliar = 0
			for curso in data['data']:
				precio1 = float(curso['quote']['USD']['price'])
				Volumen_24h1 = float(curso['quote']['USD']['volume_24h'])
				Cambio_1h1 = float(curso['quote']['USD']['percent_change_1h'])
				Cambio_24h1 = float(curso['quote']['USD']['percent_change_24h'])
				Cambio_7d1 = float(curso['quote']['USD']['percent_change_7d'])
				Capitalizacion1 = float(curso['quote']['USD']['market_cap'])
				Ultima_actualizacion1 = str(curso['quote']['USD']['last_updated'])
				models.insertInTableValor(precio1,Volumen_24h1,Cambio_1h1,Cambio_24h1,Cambio_7d1,Capitalizacion1,Ultima_actualizacion1,(ausiliar+760))
				insertar_datos(precio1, Ultima_actualizacion1,ausiliar)
				limpiar_datos(data2)
				#Escribir_datos(data2)
				ausiliar+=1
				 

 
	except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)

def temporis():
        scheduler = BlockingScheduler()
        scheduler.add_job(obtenerValor, 'interval', seconds=30)
        scheduler.start()
#primer inserto en la tabla monedas, para que no se repita
def obtenerValor1():
        temporis()
        session = Session()
        session.headers.update(headers)
        try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
                return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)


temp = obtenerValor1()

for curso in temp['data']:
	Nombre2 = str(curso['name'])
	Simbolo2 = str(curso['symbol'])
	Logo2 = str(curso['slug'])
	Fecha_añadida = str(curso['date_added'])
	Ultima_actualizacion2 = str(curso['last_updated'])
	tag2 = str(curso['tags'])
	models.insertInTableMoneda(Nombre2,Simbolo2,Logo2,Fecha_añadida,Ultima_actualizacion2,tag2)
			



