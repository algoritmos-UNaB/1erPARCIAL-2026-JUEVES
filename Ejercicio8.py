from datetime import date

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def append(self, x):
        nuevo = Nodo(x)
        act = self.header
        while act._nxt is not None:
            act = act._nxt
        act._nxt = nuevo

    def remove(self, x):
        ant = self.header
        act = self.header._nxt
        while act is not None and act._elem != x:
            ant = act
            act = act._nxt
        if act is not None:
            ant._nxt = act._nxt

    def __iter__(self):
        act = self.header._nxt
        while act is not None:
            yield act._elem
            act = act._nxt


class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada(),
            "Conveniencia": ListaEnlazada()
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = ListaEnlazada()
        self.pasillos[pasillo].append(producto)

    def remover_producto(self, id_producto):
        for lista in self.pasillos.values():
            for p in lista:
                if p.id_producto == id_producto:
                    lista.remove(p)
                    return

    def actualizar_stock(self, id_producto, nuevo_stock):
        for lista in self.pasillos.values():
            for p in lista:
                if p.id_producto == id_producto:
                    p.stock = nuevo_stock
                    return

    def remover_expirados_24hs(self):
        hoy = date.today()
        cant = 0
        for pasillo, lista in self.pasillos.items():
            nueva = ListaEnlazada()
            for p in lista:
                if (p.fecha_vencimiento - hoy).days <= 1:
                    cant += 1
                else:
                    nueva.append(p)
            self.pasillos[pasillo] = nueva
        return cant