#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Algoritmo para recuperar variaciones de precio de la bitcoin cada 30 segundos
import csv
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import requests
def ObtenerValorBtc():
        csvFile = open('bchistorical.csv', 'a')
        csvWriter = csv.writer(csvFile)

        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        textr = r.text
        splitr = textr.split(",")
        splitvalor = splitr[12].split(":")
        valor = splitvalor[1].split("}")

        #                                         TIMESTAMP                      VALOR
        csvWriter.writerow([str(datetime.datetime.now()).split('.')[0], float(valor[0]),";"])
        print ([str(datetime.datetime.now()).split('.')[0], float(valor[0])])

#generar código cada 30 segundos

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds = 30)
scheduler.start()
