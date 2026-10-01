#Defino funcion iterativa donde a son las donas que se come cada persona y b es la cantidad de personas. 
def donas_totales (a, b):
    total= 0
    for x in range(b):
        total += a
    return total 
#Para ver el total de donas consumidas debo imprimir en pantalla un llamado a la funcion y darle los parametros a y b. 
print(donas_totales(2,12))