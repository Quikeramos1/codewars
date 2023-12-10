#Funcion que elimina todas las vocales de una cadena.

def disemvowel(string_):
    lstring_=[]
    for i in string_:
        if i.lower() not in "aeiou":
            lstring_.append(i)
        else:
            continue

    string_ = "".join(lstring_)
    return string_

'''Esta solucion hace lo mismo
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")'''