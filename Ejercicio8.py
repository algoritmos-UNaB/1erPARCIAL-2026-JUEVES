class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)


#--------
    def agregar_pro(self ,dato):
        new = Nodo(dato)

        if self.header = none:
            self.header = new
            return
        
        now = self.header

        while now._nxt:
            now = now._nxt
        
        now._nxt = new
