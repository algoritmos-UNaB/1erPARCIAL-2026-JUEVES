# ProductoKwikE ; edicion , agregar , expiracion -> stock cero, etc

from datetime import date

class ProductoKwikE (self, id_producto, descripcion, marca, fecha_vencimiento, precio, stock):
    def __init__(self):
        self.id_producto = id_producto
        self.descripcion = descripcion
        self.marca = marca          #agregue
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
    
# ejercicio 6 sobrecargar __str__: Para representar el producto de forma legible 
#(ej: "Producto: Donuts Glaseadas | ID: 123 | Precio: $1.50 | Stock: 50").

#__eq__: Para comparar si dos productos son iguales basándose en su 
#id_producto y descripcion
    
    def __str__():
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: $ {self.precio} | Stock: {self.stock}"

    def __eq__(self, otro):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion


# pedia de : descripción, precio, stock;
    def edicion(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def calcularExpiracion(self, fecha_vencimiento):
        expiracion = self.fecha_vencimiento - date.today()
        if expiracion.days <= 0:
            self.stock = 0
        return expiracion.days

    #funcion adicional
    def mostrarMarca(self):
        return self.marca 

    def checkearStock(self):
        if self.stock <= 10:
            return f"Hay pocas existencias de {self.descripcion}"
        return f"Hay {self.stock} del producto {self.descripcion}"
    

    


