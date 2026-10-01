def total_interrupciones(a, b):
    # caso base: si pasaron 0, no hay interrupciones
    if b == 0:
        return 0
    # caso recursivo:  sumar las interrupciones de esta hora al restode las demas horas
    return a + total_interrupciones(a, b - 1)