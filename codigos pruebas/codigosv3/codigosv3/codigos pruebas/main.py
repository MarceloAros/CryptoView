import json


"""
data = {}
data['valorx'] = []
data['valory'] = []
data['valorx'].append(2)
data['valory'].append(3)
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
#print(data)

"""
def cargar_datos(ruta):
	with open(ruta) as contenido:
		cursos =json.load(contenido)
		print cursos['data'][0]['quote']['USD']['price']
		#print cursos['data'][2]['tags'][0]

		#print cursos['data'][0]
		#for curso in cursos['data']:
		#	tempo = list(curso.items())
		#	print str(tempo[13])
			#for x in curso:
			#	print x
			#	zips= x.items()
			#	print (zips)
				#for y in x:
				#	print (y)
		#	print('hola')

if __name__ == '__main__':
	ruta = 'ejemplo_respuesta.json'
	cargar_datos(ruta)