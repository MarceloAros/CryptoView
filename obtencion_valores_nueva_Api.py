#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import models
import sentimental_analysis
#import main

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
		'BitcoinY': [],
		'CBitcoin':[]
	},
	{
		'EthereumX': [],
		'EthereumY': [],
		'CEthereum': []
	},
	{
		'RippleX': [],
		'RippleY': [],
		'CRipple': []
	},
	{
		'LitecoinX': [],
		'LitecoinY': [],
		'CLitecoin': []
	},
	{
		'Bitcoin_CashX': [],
		'Bitcoin_CashY': [],
		'CBitcoin_Cash': []
	},
	{
		'EOSX': [],
		'EOSY': [],
		'CEOS': []
	}
]

def limpiar_datos(datos):
	if len(datos[0]['BitcoinX']) > 5 :
		data2[0]['BitcoinX'].pop(0)
		data2[0]['BitcoinY'].pop(0)
		data2[0]['CBitcoin'].pop(0)
		data2[1]['EthereumX'].pop(0)
		data2[1]['EthereumY'].pop(0)
		data2[1]['Cthereum'].pop(0)
		data2[2]['RippleX'].pop(0)
		data2[2]['RippleY'].pop(0)
		data2[2]['CRipple'].pop(0)
		data2[3]['LitecoinX'].pop(0)
		data2[3]['LitecoinY'].pop(0)
		data2[3]['CLitecoin'].pop(0)
		data2[4]['Bitcoin_CashX'].pop(0)
		data2[4]['Bitcoin_CashY'].pop(0)
		data2[4]['CBitcoin_Cash'].pop(0)
		data2[5]['EOSX'].pop(0)
		data2[5]['EOSY'].pop(0)
		data2[5]['CEOS'].pop(0)

#cambiar funcion y agregarle un parametro mas, para determinar cual dato
#agregar, y hacer la comparacion del valores, con ese nuevo parametro
def insertar_datos(precio1, Ultima_actualizacion1,ausiliar):
	#hacer la comparacion con el nuevo parametro
	#ausiliar pasa a ser una lista que tiene el id de los datos a ingresar
	#cambiar eso, en las condiciones ejem ausiliar[0],ausiliar[1], etc. 
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

def Escribir_datos(data):
        with open("data2.txt", "w") as file:
                json.dump(data, file)
        """dest=open("data.txt","w")
        for com in data:
                for i, p in com.items():
                        dest.write("%s %s \n" %(i, p))
        dest.close()"""

def Analisis_S():
	x0=sentimental_analysis.main('bitcoin')
	x1=sentimental_analysis.main('ethereum')
	x2=sentimental_analysis.main('Ripple')
	x3=sentimental_analysis.main('Litecoin')
	x4=sentimental_analysis.main('Bitcoin_Cash')
	x5=sentimental_analysis.main('EOS')
	data2[0]['CBitcoin'].append(x0)
	data2[1]['Cthereum'].append(x1)
	data2[2]['CRipple'].append(x2)
	data2[3]['CLitecoin'].append(x3)
	data2[4]['CBitcoin_Cash'].append(x4)
	data2[5]['CEOS'].append(x5)


def obtenerValor():
	session = Session()
	session.headers.update(headers)

	try:
			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			#print (json.dumps(data,indent=4))
			#insertar valor en tablas
			#cambiar valor del ausiliar segun determine el ranking (lista)
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
				Escribir_datos(data2)
				ausiliar+=1
				 

 
	except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)


#primer inserto en la tabla monedas, para que no se repita
def obtenerValor1():
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
			

scheduler = BlockingScheduler()
scheduler.add_job(obtenerValor, 'interval', minutes=30)
scheduler.start()
