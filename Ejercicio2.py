#Escribir una función iterativa que calcule la cantidad total de donas consumidas en una fiesta. 
#Recibe como parámetros dos números (naturales) a (donas por persona) y b (cantidad de personas), y devuelve el total de donas consumidas.

def Donas_Consumidas(donasxpersona, cantidadpersonas):
    total = 0

    for i in range(cantidadpersonas):
        total += donasxpersona

    return total
