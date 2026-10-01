def organizacion(eventos, expresion=True):
    if expresion:
        return sorted(eventos, reverse=True)
    return eventos
    