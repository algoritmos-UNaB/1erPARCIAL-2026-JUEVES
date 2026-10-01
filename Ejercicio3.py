def total_interrupciones (a,b):
    if b==0:
        return 0

    else:
        
        return a + total_interrupciones (a , b-1)    


    