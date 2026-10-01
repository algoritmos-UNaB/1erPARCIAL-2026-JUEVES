class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def agregar(self, dato):
        nuevo = Nodo(dato)
        actual = self.header
        while actual._nxt is not None:
            actual._nxt = actual._nxt
            actual._nxt = nuevo
        
    def remover(self, dato):
        actual = self.header
        while actual._nxt is not None:
            if actual._nxt._elem == dato:
                actual._nxt = actual._nxt._nxt
                return
                actual = actual._nxt
    
    def __iter__(self):
        actual = self.header._nxt
        while actual is not None:
        yield actual = actual._nxt
        actual = actual._nxt  