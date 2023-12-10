#Función que multiplica por 8 el valor dado por el usuario, si es par o por 9 en caso contrario.

def simple_multiplication(number):
    solucion = 0
    if number % 2 == 0:
        solucion = number * 8
    else:
        solucion = number * 9
    return solucion    