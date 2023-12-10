#Funcion que suma los númeroos positivos de una lista.

def positive_sum(arr):
    suma = []
    for i in arr:
        if i > 0:
            suma.append(i)
        else:
            continue
    resultado = sum(suma)
    return resultado
