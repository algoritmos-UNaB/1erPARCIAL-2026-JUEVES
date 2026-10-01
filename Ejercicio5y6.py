# Ejercicio 5

from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento  
        self.precio = precio
        self.stock = stock

    def cambiar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion: self.descripcion = descripcion
        if precio: self.precio = precio
        if stock: self.stock = stock

    def dias_para_expirar(self):
        dias = (self.fecha_vencimiento - date.today()).days
        if dias < 0:
            print(f"El producto '{self.descripcion}' ha expirado.")
            self.stock = 0
        return dias

    # Ejercicio 6
    
    def __str__(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"

    def __eq__(self, otro):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion