import pickle

class Vehiculo:
    marca = ''
    modelo = ''

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

vehiculo01 = Vehiculo('Toyota', 'Corolla')

#f = open('info.bin', 'wb')
#pickle.dump(vehiculo01, f)
#f.close()

f = open('info.bin', 'rb')
v01 = pickle.load(f)
f.close()

print(v01.getModelo())
