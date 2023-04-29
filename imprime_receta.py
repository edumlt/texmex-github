# imprime_receta.py

import argparse

# defino parser como mi variable de tipo argparse
parser = argparse.ArgumentParser(description='Imprime recetas')

# Configuro la estructura del argumento a introducir
parser.add_argument('file_md', metavar='file', type=argparse.FileType('r'), help='Un archivo que contenga lineas de texto')

# guardo las entradas de los argumentos en una variable args
args = parser.parse_args()

for linea in args.file_md.readlines():

	print(linea)
