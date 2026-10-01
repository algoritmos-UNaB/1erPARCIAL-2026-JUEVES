#importamos la libreria math para poder usar el metodo para calcular la raiz de 2
import math
# "n" va a ser el tamanio que le damos al diccionario
n=5
#el diccionario "Donas" se genera en base al valor de "n"
Donas = {x: x*math.sqrt(2) for x in range(1,n)}
print(Donas)