def Multiplica(*args):
    resultado = None
    for arg in args:
        valor= arg
        if resultado is None:
            resultado = valor
        else:
            resultado *= valor

    return resultado