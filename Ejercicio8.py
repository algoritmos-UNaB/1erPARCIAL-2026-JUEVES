class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def agregar(self, producto):
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(producto)
    
    def remover(self, producto):
        actual = self.header
        while actual._nxt is not None:
            if actual._nxt._elem == producto:
                actual._nxt = actual._nxt._nxt
                return actual = actual._nxt

    def __iterador__(self):
        actual = self.header._nxt
        while actual is not None:
            yield actual._elem
            actual = actual._nxt
    
    # No se si entendi bien la consigna, supongo que hay que armar todo de nuevo pero con las listas enlazadas..

class ProductoKwikE:
    def __init__(self,desc,id_p,fecha,precio,stock):
        self.descripcion=desc
        self.id_producto=id_p
        self.fecha_vencimiento=fecha
        self.precio=precio
        self.stock=stock
    #....

class KwikEMart:
    def __init__(self):
        self.pasillos={"Bebidas": ListaEnlazada(),"Snacks": ListaEnlazada(),"Conveniencias": ListaEnlazada(),}

    def agregar_pasillo(self, n_pasillo: str):
        if n_pasillo not in self.pasillos:
            self.pasillos[n_pasillo] = ListaEnlazada()
    
    def agregar_producto(self, pasillo: str, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].agregar(producto)

    def remover_producto(self, pasillo: str, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].remover(producto)

    def verificar_vencimientos(self):
        hoy = date.today()
        contador_desechos = 0
        for pasillo, productos in self.pasillos.items():
            for producto in productos[:]:
            diferencia = producto.fecha_vencimiento - hoy
            if diferencia.days <= 1:
                self.remover_producto(pasillo, producto)
                contador_desechados += 1

        return contador_desechados

