def total_interrupciones_recursivo(a, b):
    if b <= 0:
        return 0  # Caso base: Si las horas transcurridas (b) son 0, no hay interrupciones y la función devuelve 0
    return a + total_interrupciones_recursivo(a, b - 1)  # Caso recursivo: Sumamos las interrupciones de 1 hora (a) más el resultado de llamar a la función reduciendo las horas restantes en 1 

