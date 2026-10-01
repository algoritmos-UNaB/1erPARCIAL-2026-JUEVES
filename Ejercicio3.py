#Defino funcion recursiva, con caso base y caso recursivo donde a son las interrupciones por hora y b son las horas. 
def interrupciones_bart(a,b):
    if b == 0:
        return 0
    else:
        return a + interrupciones_bart(a, b-1)

#llamo la funcion a pantalla con un print y los parametros que le quiero dar. 
print(interrupciones_bart(2,4))