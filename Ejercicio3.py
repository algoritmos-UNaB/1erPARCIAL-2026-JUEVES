def bart_interrump(a, b):
    #base
    if b == 0:
        return 0
    
    return a + bart_interrump(a, (b-1))