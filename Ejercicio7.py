from datetime import date 
from Ejercicio5 import ProductoKwikE

class kwinEMart:
    def __init__(self):
        self.secciones = {
            "Bebidas": [],
            "Snacks":[],
            "Conveniencia":[]
        }
    def agregar_producto(self, seccion, producto):
        if seccion in self.secciones:
            self.secciones[seccion].append(producto)

    def remover_producto(self, seccion, producto):
        if seccion in self.secciones and producto in self.secciones[seccion]:
            self.secciones[seccion].remove(producto)
        
    def actualizar_stock(self, seccion, producto, nuevo_stock):
        if seccion in self.secciones and producto in self.secciones[seccion]:
            producto.stock = nuevo_stock
    
    def productos_por_vencer(self):
        por_vencer = []
        for seccion, productos in self.secciones.items():
            for producto in productos:
                if producto.dias_para_vencer() <= 1:
                    por_vencer.append(producto)
                    producto.marcar_stok_cero()
                    return por_vencer