from datetime import date
from Ejercicio8 import ListaEnlazada

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

        self.pasillos[pasillo].agregar(producto)

    def buscar_producto(self, id_producto):
        for productos in self.pasillos.values():
            for producto in productos:
                if producto.id_producto == id_producto:
                    return producto

        return None

    def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_producto(id_producto)

        if producto is None:
            return False

        producto.actualizar(stock=nuevo_stock)
        return True

    def remover_producto(self, id_producto):
        for lista in self.pasillos.values():
        for producto in lista:
            if producto.id_producto == id_producto:
                lista.eliminar(producto)
                return True

        return False

    def proximos_a_vencer(self):
        fecha_limite = date.today() + timedelta(days=1)
        cantidad_retirada = 0

        for productos in self.pasillos.values():
            for producto in productos[:]:
                if producto.fecha_vencimiento <= fecha_limite:
                    producto.dias_para_vencer()
                    lista.eliminar(producto)
                    cantidad_retirada += 1

        return cantidad_retirada

    def mostrar_inventario(self):
        for pasillo, productos in self.pasillos.items():
            print(f"\nPasillo: {pasillo}")

            for producto in productos:
                print(producto)