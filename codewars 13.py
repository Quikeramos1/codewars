#cuenta las vocales dadas en una cadena.

def get_count(sentence):
    vocales = ('a,e,i,o,u')
    contador = 0
    for i in sentence:
        if i.lower() in vocales:
            contador +=1
        
    return contador

'''esta función hace lo mismo:
def getCount(sentence):
    return sum(i in 'aeiou' for i in sentence)'''