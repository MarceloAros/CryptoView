from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import models

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
	'start':'1',
	'limit':'100',
}
headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': '0daaaa79-fa83-438b-a42b-f848e3e39421',
}

def obtenerValor():
	session = Session()
	session.headers.update(headers)

	try:
			response = session.get(url, params=parameters)
			data = json.loads(response.text)
			#print (json.dumps(data,indent=4))
			#insertar valor en tablas
			for curso in data['data']:
				for x in curso.get('quote').values():
					zips= x.items()
					precio1 = zips[3][1]
					Volumen_24h1 = zips[5][1]
					Cambio_1h1 = zips[6][1]
					Cambio_24h1 = zips[4][1]
					Cambio_7d1 = zips[2][1]
					Capitalizacion1 = zips[0][1]
					Ultima_actualizacion1 = zips[1][1]
		  		models.insertInTableValor(precio1,Volumen_24h1,Cambio_1h1,Cambio_24h1,Cambio_7d1,Capitalizacion1,Ultima_actualizacion1)
		  		data2 = {}
					data2['valorx'] = []
					data2['valory'] = []
					data2['valorx'].append(Ultima_actualizacion1)
					data2['valory'].append(precio1)
					with open('data.json', 'w') as file:
    				json.dump(data, file, indent=4)

 
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
			for de in curso.items():
				#print de
				Nombre2= de[2]
				Simbolo2 = de[5]
				Logo2 = de[13]
				Fecha_añadida = de[12]
				Ultima_actualizacion2 = de[1]
				tag2 = de[3]
				models.insertInTableMoneda(Nombre2,Simbolo2,Logo2,Fecha_añadida,Ultima_actualizacion2,tag2)

scheduler = BlockingScheduler()
scheduler.add_job(obtenerValor, 'interval', seconds=30)
scheduler.start()
