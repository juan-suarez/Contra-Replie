import json

nom_archivo='/imagenes/mapa/mapa.json'
with open(nom_archivo) as archivo:
    datos=json.load(archivo)


capas=datos['layers']


obstaculos = capas[0]['data']

print(obstaculos)