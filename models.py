"""from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), unique=True)
#class nombre de mi modelo """

#funcion de insersion de datos

import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def insertInTableValor(Precio,Volumen_24h,Cambio_1h,Cambio_24h,Cambio_7d,Capitalizacion,Ultima_actualizacion):
	try:
		connection = mysql.connector.connect(host='localhost',
							 database='mydb',
							 user='root',
							 password='Cryptoview')
		cursor = connection.cursor(prepared=True)
		sql_insert_query = """ INSERT INTO 'valor'
					  ('Precio', 'Volumen_24h', 'Cambio_1h', 'Cambio_24h', 'Cambio_7d', 'Capitalizacion', 'Ultima_actualizacion') VALUES (%s,%s,%s,%s,%s,%s,%s)"""
		insert_tuple = (Precio, Volumen_24h, Cambio_1h, Cambio_24h, Cambio_7d, Capitalizacion, Ultima_actualizacion)
		result  = cursor.execute(sql_insert_query, insert_tuple)
		connection.commit()
		print ("Record inserted successfully into python_users table")
	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to insert into MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")

def insertInTableMoneda(Nombre,Simbolo,Logo,Fecha_añadida,Ultima_actualizacion,tag):
	try:
		connection = mysql.connector.connect(host='localhost',
							 database='mydb',
							 user='root',
							 password='Cryptoview')
		cursor = connection.cursor(prepared=True)
		sql_insert_query = """ INSERT INTO 'moneda'
					  ('Nombre', 'Simbolo', 'Logo', 'Fecha_añadida', 'Ultima_actualizacion', 'tag') VALUES (%s,%s,%s,%s,%s,%s)"""
		insert_tuple = (Nombre, Simbolo, Logo, Fecha_añadida, Ultima_actualizacion, tag)
		result  = cursor.execute(sql_insert_query, insert_tuple)
		connection.commit()
		print ("Record inserted successfully into python_users table")
	except mysql.connector.Error as error :
		connection.rollback()
		print("Failed to insert into MySQL table {}".format(error))
	finally:
		#closing database connection.
		if(connection.is_connected()):
			cursor.close()
			connection.close()
			print("MySQL connection is closed")            

