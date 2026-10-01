# Nodo 
class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None 


# Iterador
class IteradorListaEnlazada:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if not self.actual:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato


# Lista Enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def __iter__(self):
        return IteradorListaEnlazada(self.cabeza)


# Integración del Kwik-E-Mart usando la Lista Enlazada
class KwikEMart:
    def __init__(self):
       
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].agregar(producto)

    def remover_producto(self, id_producto):
        for pasillo, lista in self.pasillos.items():
            nueva_lista = ListaEnlazada()
            for prod in lista:  
                if prod.id_producto != id_producto:
                    nueva_lista.agregar(prod)
            self.pasillos[pasillo] = nueva_lista

    def desechar_expirados_24hs(self):
        for pasillo, lista in self.pasillos.items():
            nueva_lista = ListaEnlazada()
            for prod in lista:
                if prod.dias_para_expirar() > 1:
                    nueva_lista.agregar(prod)
            self.pasillos[pasillo] = nueva_lista