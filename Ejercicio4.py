# funcion si True lista de Z a A, si False o "nada" lista A a Z
#nota: pedia "eventos" como nombre de variable para las listas
#sorted -> true = ordena de z a a (al reves)
#sorted ordena de A a Z

def ordenar (eventos, expresion=False):
    if expresion:
        return sorted(eventos, reverse = True)
    return sorted(eventos)

eventos = ["festival", "navidad", "pascua", "año nuevo"]
print (ordenar(eventos))
print (ordenar(eventos, True))