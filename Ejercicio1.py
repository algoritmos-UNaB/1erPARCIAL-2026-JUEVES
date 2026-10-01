##Generar una lista por compresión que contenga la cantidad de donas que Homero consume en el infierno.
##Por cada dona que Homero consume apareceran más donas al ritmo de raíz de dos donas ( 22) en su suplicio hasta que reviente.
## Ejemplo: { 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }


from math import sqrt
def cant_donas ( cantidad ):
    return { 
        n:n / sqrt(2)
        for n in range (1, cantidad + 1 )
    }

print(cant_donas(8))