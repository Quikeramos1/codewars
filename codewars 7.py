#Funcion que convierte horas, minutos y segundos en milisegundos y devuelve el total.

def past(h, m, s):
    hms= h* 3600000
    mms = m * 60000
    sms = s * 1000
    return hms + mms + sms