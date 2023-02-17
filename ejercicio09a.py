#Crea un script que le pida al usuario una lista de países (separados por comas). 
#Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
#Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

paises = list(input('Ingrese una lista de paises separados por ", ": ').split(','))

list_paises = map(str.strip, paises)

paises_set = set(list_paises)

print(type(paises), ':', paises)
print(type(list_paises), ':', list_paises)
print(type(paises_set), ':', paises_set)
