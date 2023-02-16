class Alumno:
    def __init__(self):
        pass
    
    _nombre = ''
    _nota= ''

    def nombreAlumno(self, nombre):
        print('Nombre: ', nombre)

    def notaAlumno(self, nota):
        if nota>6:
            print('Nota:', nota, '- APROBADO')
        else:
            print('Nota:' , nota, '- DESAPROBADO')
    
    

alumno_1 = Alumno()

alumno_1.nombreAlumno('Jose')
alumno_1.notaAlumno(5)

alumno_2 = Alumno()

alumno_2.nombreAlumno('Marita')
alumno_2.notaAlumno(8)