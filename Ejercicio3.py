#La Paciencia de Marge

def interupcion (a:int,b:int)->int:
    if b==0:
        return 0
    return a+interupcion(b-1)


