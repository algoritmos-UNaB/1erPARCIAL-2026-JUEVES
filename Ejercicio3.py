#Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge. 
#Recibe como parámetros dos números (naturales) a (interrupciones por hora) y b (horas de la tarde), y devuelve el total de interrupciones.

def Paciencia_Marge(interrupcionexhora, horasdelatarde):
    if horasdelatarde == 0:
        return 0
    return interrupcionexhora + Paciencia_Marge(interrupcionexhora, horasdelatarde - 1)
