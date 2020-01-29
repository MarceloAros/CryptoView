
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

def insertInTableValor(Precio,Volumen_24h,Cambio_1h,Cambio_24h,Cambio_7d,Capitalizacion,Ultima_actualizacion, Moneda_idMoneda):
	try:
		connection = mysql.connector.connect(host='localhost',
							 database='mydb',
							 user='root',
							 password='Cryptoview')
		cursor = connection.cursor(prepared=True)
		sql_insert_query = """ INSERT INTO Valor (Precio, Volumen_24h, Cambio_1h, Cambio_24h, Cambio_7d, Capitalizacion, Ultima_actualizacion, Moneda_idMoneda) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
		insert_tuple = (Precio, Volumen_24h, Cambio_1h, Cambio_24h, Cambio_7d, Capitalizacion, Ultima_actualizacion, Moneda_idMoneda)
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
		sql_insert_query = """ INSERT INTO Moneda (Nombre, Simbolo, Logo, Fecha_añadida, Ultima_actualizacion, tag) VALUES (%s,%s,%s,%s,%s,%s)"""
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

"""
def recuperar_valores():
	try:
		connection = mysql.connector.connect(host='localhost',database='mydb',user='root',password='Cryptoview')
		sql_select_Query = "select * from Valor"
		cursor = connection.cursor()
		cursor.execute(sql_select_Query)
		records = cursor.fetchall()
		print("Total number of rows in Valor is: ", cursor.rowcount)

		print("\n")
		for row in records:
			print("Id = ", row[0], )
			print("Precio = ", row[1])
			print("Volumen_24h  = ", row[2])
			print("Cambio_1h  = ", row[3])
			print("Cambio_24h  = ", row[4])
			print("Cambio_7d  = ", row[5])
			print("Capitalizacion  = ", row[6])
			print("Ultima_actualizacion  = ", row[7], "\n")

	except Error as e:
		print("Error reading data from MySQL table", e)
	finally:
		if (connection.is_connected()):
			connection.close()
			cursor.close()
			print("MySQL connection is closed")

recuperar_valores()"""