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
            actual = actual._nxt

        actual._nxt = nuevo

    def __iter__(self):
        actual = self.header._nxt

        while actual is not None:
            yield actual._elem
            actual = actual._nxt

    def remover(self, dato):
        anterior = self.header
        actual = self.header._nxt

        while actual is not None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                return

            anterior = actual
            actual = actual._nxt


