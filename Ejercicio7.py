# clase KwikEMart, lista de objetos ProductoKwikE; control de stock
# expiracion , etc.
from datetime import date

class KwikEMart:
    def __init__(self):
        self.pasillos: {
            "Bebidas":[],
            "Snacks":[],
            "Galletitas":[],
            "Fideos":[]    
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
    
    