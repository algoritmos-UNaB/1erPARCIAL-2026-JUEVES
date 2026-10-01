def ordenar(eventos,ord_descendiente=False):
    return sorted(eventos, reverse=ord_descendiente)

eventos = ['Kermés', 'Concurso de comida', 'Reunión del Concejo Municipal']
print(ordenar(eventos))
