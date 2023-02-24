import sqlite3
import getpass


def main():
    crear_usuario(4, 'Jose', 'claveJose')


def main_():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Login INCORRECTO')


def verifica_credenciales(username, password):
    conn = sqlite3.connect('B:\OpenBootCamp\Python\python_basico\ejercicio11_clase\micarpeta.db')
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username = "{username}" AND password = "{password}"'
    print('Query a ejecutar', query)

    rows = cursor.execute(query)

    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False
    return True


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('B:\OpenBootCamp\Python\python_basico\ejercicio11\micarpeta.db')
    cursor = conn.cursor()

    query = """INSERT INTO users (id, username, password) VALUES (?, ?, ?)""" 
    print('Query a ejecutar', query)

    rows = cursor.execute(query, (identificador, usuario, clave))

    print(type(rows))

    conn.commit()

    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()
