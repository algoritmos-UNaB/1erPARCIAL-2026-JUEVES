## Ejercicio 8: La Gestión del Kwik-E-Mart

from Ejercicio5 import ProductoKwikE
from datetime import date

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
    def append(self, dato):
        actual = self.header
        while actual._nxt:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
    def remover(self, dato):
        actual = self.header
        while actual._nxt:
            if actual._nxt._elem == dato:
                actual._nxt = actual._nxt._nxt
                return True
            actual = actual._nxt
        return False
    def __iter__(self):
        actual = self.header._nxt
        while actual:
            yield actual._elem
            actual = actual._nxt