def anio_bisiesto(anio):
    if((anio%400==0 or anio%4==0) and (anio%100!=0)):
        print('Es bisiesto')
    else:
        print('NO es bisiesto')

anio_bisiesto(2025)

