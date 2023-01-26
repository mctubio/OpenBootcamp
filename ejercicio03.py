peso = float(input('Cual es tu peso en kilos?'))

altura = float(input('Cual es tu altura en metros?'))

IMC = round(peso/altura/altura, 2)

print('Tu IMC es: ' + str(IMC))
