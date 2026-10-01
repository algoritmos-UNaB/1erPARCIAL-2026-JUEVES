def organizar_eventos(eventos, expresion=False):
    """eventos: lista de cadenas """
    """expresion: booleano (True -> Descendente Z-A, False -> Ascendente A-Z)"""

    return sorted(eventos, reverse=bool(expresion))
