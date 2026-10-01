class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class iteradorlista_enlazada :
    def __init__(self, primer_nodo)
        self.actual = primer_nodo

    def __itter__ (self) :
        return self

    def __next__( self) : 
        if self.actual is None
            raise stopiteration       

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)