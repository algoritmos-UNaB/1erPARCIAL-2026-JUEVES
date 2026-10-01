def contar_donas(donas: int,personas: int):
    contador=0

    for i in range (personas):
        contador += donas
    return contador

print(contar_donas(3,5))