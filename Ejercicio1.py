import math

# Si el prototipo requiere una lista por comprensión:
donas_lista = [(math.sqrt(2)) ** (n - 1) for n in range(1, 11)]

# Si el prototipo requiere un diccionario por comprensión:
donas_dict = {n: (math.sqrt(2)) ** (n - 1) for n in range(1, 11)}