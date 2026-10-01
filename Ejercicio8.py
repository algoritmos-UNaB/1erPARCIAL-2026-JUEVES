from datetime import datetime, timedelta
from ejercicio6 import ProductoKwikE_


class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class IteradorListaEnlazada:
    def __init__(self,primero):
        self.actual = primero
    def __next__(self):
        if self.actual is None:
            raise StopIteration('No hay mas elementos en la listas')
        dato = self.actual._elem 
        self.actual = self.actual._nxt 
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
    def append(self, dato):
        actual = self.header
        while actual._nxt is not None:
            actual = actual._nxt
        actual._nxt = Nodo(dato)
    def remove(self,dato):
        anterior = self.header
        actual = self.header._nxt
        while actual is not None:
            if actual._elem == dato:
                anterior._nxt = actual._nxt
                return True
            anterior = actual
            actual = actual._nxt 
        raise ValueError("elemento no encontrado en la lista")
    def __iter__(self):
        return IteradorListaEnlazada(self.header._nxt)

    def __bool__(self):
        return self.header._nxt is not None

class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": ListaEnlazada(),
            "Snacks": ListaEnlazada()
        }
    def aniadir_producto(self, producto, pasillo):
            if pasillo not in self.pasillos:
                self.pasillos[pasillo] = ListaEnlazada()
            self.pasillos[pasillo].append(producto)
            print(f"producto: {producto.descripcion} id: {producto.id_producto} añadido a {pasillo}")
    
    def remover_producto(self, id_producto):
            for nombre_pasillo, lista_productos in self.pasillos.items():
                for producto in lista_productos:
                    if producto.id_producto == id_producto:
                        lista_productos.remove(producto)
                        print(f"Producto {id_producto} Borrado.")
                        return True
            print(f"error: producto con id {id_producto} no encontrado")
            return False

    def actualizar_stock(self, id_producto, nuevo_stock):
            for lista_productos in self.pasillos.values():
                for producto in lista_productos:
                    if producto.id_producto == id_producto:
                        producto.cambiar(stock=nuevo_stock)
                        print(f'Stock de {id_producto} actualizado a {nuevo_stock}')
                        return True

    def remover_proximos_expirar(self):
            total_removidos = 0
            ahora = datetime.now()
            limite = ahora + timedelta(hours=24)
            for nombre_pasillo, lista_productos in self.pasillos.items():
                productos_mantener = ListaEnlazada()
                for producto in lista_productos:
                    if producto.fecha_vencimiento <= limite:
                        total_removidos +=1
                        print(f'Producto Removido: {producto.descripcion} id: {producto.id_producto}de {nombre_pasillo} - Expira en menos de 24 horas')
                    else:
                        productos_mantener.append(producto)
                self.pasillos[nombre_pasillo] = productos_mantener
            return total_removidos
    def mostrar_inventario(self):
            print("INVENTARIO")
            for pasillo, lista_productos in self.pasillos.items():
                if lista_productos:
                    print(f'{pasillo}')
                    for producto in lista_productos:
                        print(f'{producto}')