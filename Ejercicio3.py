def total_interrupciones(a, b):
    if b == 0:
        return 0
    else:
        b = b - 1
        resultado = a + total_interrupciones(a, b)
        return resultado