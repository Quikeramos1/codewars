#Esta función devuelve True si el final de la cadena dada en el primer argumento, termina con la cadena dada en el segundo argumento.


def solution(text, ending):
    if text == ending:
        return True
    elif len(text)< len(ending):
        return False
    else:
        text = list(text)
        ending = list(ending)
        contador = -1
        len_ending = len(ending)
        while len_ending > 0:
            if text[contador] == ending[contador]:
                contador -=1
                len_ending = len_ending -1
            else:
                return False
        return True




