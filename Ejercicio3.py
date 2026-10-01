def tiempo_interrupciones(a,b):
    if b == 0:
        return 0
    else:
        return a + tiempo_interrupciones(a, b-1)