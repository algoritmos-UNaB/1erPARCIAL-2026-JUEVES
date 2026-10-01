# definimos la funcion interrupciones que recibe dos parametros a(interrupciones por hora) y b(horas de la tarde)
def interrupciones(a,b):
#generamos un condicional para que si b es igual a 1, retorne a, de lo contrario retorne a + interrupciones(a,b-1)
#lo que repite la funcion hasta que b sea igual a 1 y a su vez sume a cada iteracion el valor de a    
    if b == 1:
        return a
    else:
        return a + interrupciones(a, b-1)