from Operadores import Sumador as suma
from Operadores import Restador as resta
from Operadores import Multiplicador as multi
from Operadores import Divisor as divi

def main():
    adiccion = suma.Suma(2,2,8,8)
    print(adiccion)

    sustraccion = resta.Resta(20,6,4, 5)
    print(sustraccion)

    multiplicar = multi.Multiplica(4,5,2)
    print(multiplicar)

    dividir = divi.Divide(20,10,5)
    print(dividir)

if __name__ == '__main__':
    main()