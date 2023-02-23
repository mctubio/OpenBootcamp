import sqlite3
import getpass

def main():
    nombre = input('Ingrese el nombre del estudiante: ')
    apellido = input('Ingrese el apellido del estudiante: ')
    if buscar_estudiante(nombre, apellido):
        print('Es un/a estudiante')
    else:
        print('No es un/a estudiante')


def nuevo_estudiante():
    conn = sqlite3.connect('B:\OpenBootCamp\Python\python_basico\ejerciocio11_entrega\data_escuela.db')   
    cursor = conn.cursor()

    id = input('Ingrese el codigo del nuevo estudiante: ')
    nombre = input('Ingrese el nombre del nuevo estudiante: ')
    apellido = input('Ingrese el apellido del nuevo estudiante: ')

    query = """INSERT INTO alumnos(id, nombre, apellido) VALUES (?,?,?)"""
    #print('la query es: ', query)
    rows = cursor.execute(query, (id, nombre, apellido))
    
    print(type(rows))

    conn.commit()
    cursor.close()
    conn.close()

def buscar_estudiante(nombre, apellido):
    conn = sqlite3.connect('B:\OpenBootCamp\Python\python_basico\ejerciocio11_entrega\data_escuela.db')   
    cursor = conn.cursor()

#    nombre = input('Ingrese el nombre del estudiante: ')
#    apellido = input('Ingrese el apellido del estudiante: ')

    query = f'SELECT id FROM alumnos where nombre="{nombre}" AND apellido="{apellido}"'

    #print('la query es: ', query)

    rows = cursor.execute(query)
    
    data = rows.fetchone()


    cursor.close()
    conn.close()

    if data == None:
        return False
    return True


if __name__ == '__main__':
    main()