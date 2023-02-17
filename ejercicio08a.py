def main():
    f = open('mi_archivo.txt', 'x')
    
    lista=[
        'primera linea',
        'segunda linea',
        'ultima linea'
    ]

    escribe('mi_archivo.txt', lista)



def escribe(fichero, datos):

    f= open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea= linea +'\n'
        f.write(linea)
        
    f.close()
        



if __name__=='__main__':
    main()