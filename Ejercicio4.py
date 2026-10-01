#definimos la variable de eventos con los parametros fijados en lista de strings y un booleano
def eventos(i:list[str],ii:bool):
#creamos una condicon para ordenar la lista de strings de manera ascendente o descendente dependiendo del booleano
# utilizando la funcion sorted() para ordenar la lista de strings    
    if ii:
        i= sorted(i, reverse=True)
    else:
        i= sorted(i)
    return i
    