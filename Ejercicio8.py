class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class IteradorLista:
    def __init__(self, nodo_inicial):
        self._actual = nodo_inicial

    def __iter__(self):
        return self

    def __next__(self):
        if self._actual is None:
            raise StopIteration
        dato = self._actual._elem
        self._actual = self._actual._nxt
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def agregar(self, dato):
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
        self.header._elem += 1

    def remover(self, dato):
        anterior = self.header
        actual = self.header._nxt
        while actual is not None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                self.header._elem -= 1
                return True
            anterior = actual
            actual = actual._nxt
        return False

    def __len__(self):
        return self.header._elem

    def __iter__(self):
        return IteradorLista(self.header._nxt)

nombre y apellido: joaquin ramonet

email: joaquinramonet1@gmail.com

comision: num 2 (jueves de 8 a 12 hs)