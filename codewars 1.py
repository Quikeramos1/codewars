#Funcion para obtener el número de posicion de un texto dado por el usuario y devolverlo como cadena

def alphabet_position(text):
    text = text.lower()
    alph_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 
                 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
                 'z':26}
    lsolucion = []
    for letra in text:
        if letra in alph_dict:
            lsolucion.append(alph_dict[letra])
        else:
            continue
    
       
    fsolucion = str(lsolucion)
    fsolucion = fsolucion.replace(',', '')
    fsolucion = fsolucion.replace('[',"")
    fsolucion = fsolucion.replace(']',"")
            
    
    return fsolucion    
    
    
                
text = input("introduce el texto a procesar: ")
solucion = alphabet_position(text)
print(str(solucion))

