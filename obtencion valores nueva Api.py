from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apscheduler.schedulers.blocking import BlockingScheduler

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
  		print(response.text)
  		data = json.loads(response.text)
 
	except (ConnectionError, Timeout, TooManyRedirects) as e:
  		print(e)

scheduler = BlockingScheduler()
scheduler.add_job(obtenerValor, 'interval', seconds=10)
scheduler.start()
#print(data)