#Función que devuelve el número de True de una lista.

def count_sheeps(sheep):
    
    contador = 0
    if len(sheep)== 0:
        return 0
    elif True not in sheep:
        contador = 0
    for i in sheep:
        if i == True:
            contador +=1
            
    return contador

sheep = []
print(count_sheeps(sheep))

'''
Esta función hace lo mismo:
def count_sheeps(sheep):
  return sheep.count(True)
'''




