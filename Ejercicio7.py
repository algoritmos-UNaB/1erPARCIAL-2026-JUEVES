from datetime import datetime 
class KwikEMart:
    def __init__ (self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

    def agregar_producto (self, pasillo, producto):
        pasillo.append (producto)

    def remover_producto (self, pasillo, producto):
        if producto in pasillo:
            pasillo.remove (producto)
    def actualizar_stock (self, producto, nuevo_stock):
        producto.stock = nuevo_stock