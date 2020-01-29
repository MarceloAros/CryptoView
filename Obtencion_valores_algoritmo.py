#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from apscheduler.schedulers.blocking import BlockingScheduler



url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical'
parameters = {
	'id':'1',
	'time_start':'2019-01-01',
	'time_end':'2019-01-03'
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
			print (data)
	except (ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)

obtenerValor()