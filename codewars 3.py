#Funcion que devuelve una lista cuya posicion 0 es el valor de len de numeros positivos y la posicion 1 
# es la suma de todo los números negativos dados por el usuario en una lista 

def count_positives_sum_negatives(arr):
    pos=[]
    lpos=0
    neg=0
    resultado=[]
    if len(arr) == 0 or arr == False:
        solucion = []
    else:    
        for n in arr:
            if n>0:
                pos.append(n)
                lpos = len(pos)
                
                lpos= int(lpos)
                
                
            else:
                neg += n
                neg = int(neg)
        
        resultado.append(lpos)
        resultado.append(neg)
     
     
    return resultado


arr = [-1,2,5,-5,8,-10,-90,5,9,1,1] #sustituir por: arr = input("Introduce la lista a procesar: ")
solucion = count_positives_sum_negatives(arr)
print(solucion)