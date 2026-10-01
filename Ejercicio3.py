def interrupciones_bart(interrupciones: int,horas: int):
    if horas<=0:
        return 0
    

    return interrupciones + interrupciones_bart(interrupciones,horas-1)

print(interrupciones_bart(3,5))