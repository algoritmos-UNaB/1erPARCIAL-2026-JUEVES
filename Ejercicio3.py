##Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge. 
## Recibe como parámetros dos números (naturales) a (interrupciones por hora) y b (horas de la tarde),
## y devuelve el total de interrupciones.

def inte_marge (a , b):
     if a < 0 or b<0:
        return("valores invalidos")

    if b == 0:
        return 0

return a + inte_marge(a, b-1 )

a = int(input ("Ingrese las interrupciones por hora ")) 
b = int(input ("Ingrese lashoras de la tarde "))

resultado  = inte_marge (a, b)

print("Resultado: " , resultado )