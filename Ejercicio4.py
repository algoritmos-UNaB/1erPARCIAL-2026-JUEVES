def eventos_ordenados(eventos:list, booleano=False):
    return sorted(eventos,reverse=booleano)

lista_eventos = ["Kermes", "Concurso de Comida", "Reunion del concejo municipal"]

print(eventos_ordenados(lista_eventos, True))
print(eventos_ordenados(lista_eventos))

