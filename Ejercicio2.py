def total_consum(a , b):
    total = 0

    for i in range(b):
        total = total + a
    return total

#por ejemplo envio estos valores
total_donas = total_consum( 5,5 )
print(total_donas)