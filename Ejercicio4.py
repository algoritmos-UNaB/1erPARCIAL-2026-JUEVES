def orgarizar_eventos (eventos, descendente=false):
    # si la expresion es true, se ordena de Z a A (reverse=true)
    # si es falso (o por defecto), se ordena de A a Z (reverse=false)
    return total (eventos, reserve=descendente)