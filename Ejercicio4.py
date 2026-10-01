## Ejercicio 4: La Organización de Springfield (Condicional)

def organizar_eventos(eventos, descendente=False):
    if descendente:
        return sorted(eventos, reverse=True)
    else:
        return sorted(eventos)
