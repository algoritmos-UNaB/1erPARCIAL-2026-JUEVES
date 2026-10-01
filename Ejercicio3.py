#F Recursiva, a (interrupciones por hora) y b (horas de la tarde), 
#y devuelve el total de interrupciones.

def interrupRecursivo(a, b):
    if b == 0:
      return 0
    return a + interrupRecursivo(a, b-1)

#Ejemplo rapido 3 y 5 darian 15 va sumando de a 3 unas b=5
print(interrupRecursivo(3,5))