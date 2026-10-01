#Defino una funcion condicional que ordena alfabeticamente ascendientemente por defecto, caso contrario ordena la lista de forma descendiente
def ordeno_eventos(eventos, expresion = False): #por defecto lo dejo como false porque así lo pide la consigna
    if expresion: #la funcion entra al if solo si expresion es True
        return sorted(eventos, reverse=True) #sorted ordena alfabeticamente de forma ascendiente por eso agrego el reverse =True para que ordene de forma descendiente
    else:
        return sorted(eventos)
