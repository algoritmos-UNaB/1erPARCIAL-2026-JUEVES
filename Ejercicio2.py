# Funcion Iterativa, B= cantidad de personas, A = donas por persona 
def donasIterativo (a, b):
    total = 0
    for n in range (b):
        total += a
    return total

a = int(input("Ingrese cuantas donas come una persona: "))
b = int(input("Ingrese cuantas personas hay: "))
