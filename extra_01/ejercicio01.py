import os
from os.path import getsize

descargas = os.scandir('C:/Users/bebuc/Downloads')

print(descargas)

for archivo in descargas:
    if archivo.is_file():
        print('Nombre: ', archivo, 'Tamaño: ',getsize(archivo))