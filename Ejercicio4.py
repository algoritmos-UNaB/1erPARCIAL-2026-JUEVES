def ordenar_eventos(eventos, expresion = False):
if expresion:
    return sorted(eventos, reverse = True)
    else:
        return sorted(eventos)

## ejm #uso
        lista_eventos = ["kermes", "concurso de comida", "reunion municipal"]
        print(ordenar_eventos(lista_eventos))
        print(ordenar_eventos(lista_eventos, True))
         