# definimos la funcion "cant_donas" con los parametros "a" (donas por persona) y "b"(cantidad de personas) 
def cant_donas(a,b):
#inicializamos la variable "donas_total" en 0
    donas_total = 0
#el bucle for se ejecuta la cantidad de veces de "b" sumando el valor de "a" en cada iteracion
    for i in range(b):
        donas_total = donas_total + a
#la funcion retorna el valor almacenado en "donas_total"
    return donas_total