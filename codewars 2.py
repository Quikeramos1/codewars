#Función que devuelve la suma de una lista dada por el usuario

def sum_array(a):
    if len(a) == 0:
        solucion = 0
    elif len(a) == 1:
        solucion = a[0]
    else:
        solucion = sum(a)
        try:
            int(solucion)
        except:
            solucion = float(solucion)
    print(solucion)
    
    
    
a = [0,10,9.8,-5] #sustituir por: a = input("Introduce la lista a procesar: ")

sum_array(a)