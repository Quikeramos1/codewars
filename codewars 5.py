#Funcion que imprime tantas obejas como el usuario introduzca como número entero (debe ser positivo)

def count_sheep(n):
    if n <= 0:
        return ""
    else:
        lsheep = []
        for i in range(1,n+1): 
            i= str(i)
            lsheep.append(i +" sheep...")

    lsheep = "".join(lsheep)
              
    return lsheep    


           
        
    

print( count_sheep(11))