##Escribir una función que reciba dos parámetros: 
##(i) una lista desordenada de "eventos" (ej: "Kermés", "Concurso de Comida", "Reunión del Concejo Municipal");
## y (ii) una expresión booleana (que puede ser evaluada a True o False).
## Si el valor de la expresión es True, la lista de eventos se ordenará alfabéticamente en 
#orden descendente (de la Z a la A). En caso contrario, se ordenará de forma ascendente (de la A a la Z).
##Por defecto, si la función es llamada sin una "expresión" (solo la lista de eventos), 
## la lista debe retornar ordenada de forma ascendente.

def ordenar_eventos(eventos, descendente=False):
    return sorted(eventos, reverse=descendente)


eventos = ["Kermés", "Concurso", "Reunión"]

print(ordenar_eventos(eventos))