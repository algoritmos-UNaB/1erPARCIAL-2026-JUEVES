Eventos = ["kermes", "baile", "reunion municipal", "asambla", "concurso de comida"]

def ordenamiento(Eventos, descendente = False):
  if descendente == False:
     Eventos.sort()
  else:
    Eventos.sort(reverse = True)
    
  return Eventos

ordenamiento(Eventos, descendente = False)
resultado = ordenamiento(Eventos)
print(resultado)