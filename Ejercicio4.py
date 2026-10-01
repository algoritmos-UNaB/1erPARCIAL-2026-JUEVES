eventos = ["Kermes","Concurso de comida", "Reunion del Concejo Municipal"]

def ordenar_eventos(eventos:list, expression: bool= False):
    if not isinstance (expression, bool):
        raise TypeError("La expresion debe ser un booleano")
    ordenados []
    for evento in eventos:
        ordenados.append(evento)
    ordenados.sort(reverse=expression)
    return ordenados
print(ordenar_eventos(eventos))
print(ordenar_eventos, True)