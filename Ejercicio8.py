# aplicar Lista enlazada a clase KwikEMart

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class Iterador:
    def __init__(self, nodo):
        self.actual = nodo

    def __next__(self):
        if self.actual is None:
            raise StopIteration

        dato = self.actual._elem
        self.actual = self.actual._nxt
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)   
    
    def agregar(self, dato):
        nuevo = Nodo(dato)
        nuevo._nxt = self.header
        self.header = nuevo
    
    def eliminar (self, dato):
        actual = self.header
        anterior = None

        while actual is not None:
            if actual._elem == dato:
                if anterior is None:
                    self.header = actual._nxt
                else:
                    anterior._nxt = actual._nxt
                return

            anterior = actual
            actual = actual._nxt

    def __iter__():
        return Iterador(self.header)


#copie y pegue el anterior pero con listas
from datetime import date

class KwikEMart:
    def __init__(self):
        self.pasillos: {
            "Bebidas":ListaEnlazada(),
            "Snacks":ListaEnlazada(),
            "Galletitas":ListaEnlazada(),
            "Fideos":ListaEnlazada()    
            }
    
    def agregarProducto (self, pasillo, producto ):
        self.pasillos[pasillo].append(producto)

    def actualizStock (self, producto, nuevoStock):
        producto.stock = nuevoStock
        
    def eliminarProducto (self, pasillo, producto):
        self.pasillos[pasillo].remove(producto)

    def expiracionHoras():
        expirados = 0
        for pasillo in self.pasillos.values(): 
            for producto in pasillo:
                dias = (producto.fecha_vencimiento - date.today()).days
                if dias <= 1:
                    pasillo.remove(producto)
                    expirados += 1
        return expirados

    #funcion adicional
    def pocosProductosStock(self):
        contador = 0

        for pasillo in self.pasillos.values():
            for producto in pasillo:
                if producto.stock <= 10:
                    contador += 1
        return contador

    def agregarPasillo (self, nuevoPasillo):
            self.pasillos[nuevoPasillo] = []

    def cantidadPasillos (self):
            return len(self.pasillos)