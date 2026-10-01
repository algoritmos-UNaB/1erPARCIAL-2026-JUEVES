import math
N = 8   
donas = {n: math.sqrt(2) ** (n - 1) for n in range(1, N + 1)}

print(donas)
