def interrupciones_bart (a,b) :
    #caso baso, 0 interrupciones, devuelve 0
    if b == 0 : 
        return  0

    #recursivo
    return a + interrupciones_bart ( a , b - 1 )    