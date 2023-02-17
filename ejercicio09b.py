#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada 
#por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

numeros_str = list((input('Ingrese una lista de numeros", ": ').split(',')))

numeros = [int(x) for x in numeros_str]

pares = list(filter(lambda x: x%2 ==0, numeros))

suma = reduce(lambda a, b: a+b, pares)

print(f'Los numeros ingresados son {numeros}, los pares {pares} y la suma de estos da {suma}')
