def ordenar_eventos(eventos, descendente=False):
    if descendente == True:
        eventos_ordenados = sorted(eventos, reverse=True)
        return eventos_ordenados
    elif descendente == False:
        eventos_ordenados = sorted(eventos, reverse=False)
        return eventos_ordenados