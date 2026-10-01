ef interrupciones_tot(a,b):
  if b == 0:
    return 0
  return a + interrupciones_tot(a,b-1)

   
print(interrupciones_tot(3,7))