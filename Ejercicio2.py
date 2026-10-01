a= int(input("Cant. de donas consumidas: "))
b= int(input("Cant. de personas: "))
def total_donas(a,b):
    total= 0
    for x in range (b):
        total+= a
    return total
print("Total de donas: ", total_donas(a,b))