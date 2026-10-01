## Ejercicio 7: La Gestión del Kwik-E-Mart

from datetime import date

class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": []
            "Snacks": []
            "Conveniencia": []
        }
    def añadir_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)
    def remover_producto(self, producto_id):
        for pasillo, lista_productos in self.pasillos.items():
            for producto in lista_productos:
                if producto.id_producto == producto_id
                    lista_productos.remover(producto)
                    return
    def actu_stock(self, producto_id, nuevo_stock):
        for lista_productos in self.pasillos.values():
            for producto in lista_productos:
                if producto.id_producto == producto_id:
                    producto.stock = nuevo_stock
                    return
    def expiran_24h(self):
        hoy = date.today()
        for pasillo, lista_productos in self.pasillos.items():
            self.pasillos[pasillo] = [
                p for p in lista_productos if (p.fecha_vencimiento - hoy).days > 1
            ] 
