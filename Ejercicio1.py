#Generar una lista por compresión que contenga la cantidad de donas que Homero consume en el infierno. Por cada dona que Homero consume apareceran más donas al ritmo de raíz de dos donas (
2 2) en su suplicio hasta que reviente.

#Ejemplo: { 1: 1, 2: 1.41421356237, 3: 2, 4: 2.82842712475, 5: ... }
from math import sqrt
donas = [sqrt(2)**i for i in range (10)]
print(donas)
