##Escribir una función iterativa que calcule la cantidad total de donas consumidas en una fiesta. 
##Recibe como parámetros dos números (naturales) a (donas por persona) y b (cantidad de personas),
## y devuelve el total de donas consumidas.


def donas_totales (a, b) :
    if a < 0 or b<0:
        return("valores invalidos")

    total = 0 

    for _ in range (b): 
        total += a 

    return total 

a = int(input ("Ingrese las donas por persona ")) 
b = int(input ("Ingrese la cantidad de personas "))

resultado  = donas_totales (a, b)

print("Resultado: " , resultado )


    
