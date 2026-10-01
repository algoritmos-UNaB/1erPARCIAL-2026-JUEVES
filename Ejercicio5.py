from datetime import date

class ProductoKwikE:

    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def CambiarDato(self, descripcion=None, precio=None, stock=None):

        if descripcion is not None:
            self.descripcion = descripcion

        if precio is not None:
            self.precio = precio

        if stock is not None:
            self.stock = stock

    def dias_vencimiento(self):
        hoy = date.today()
        dias = (self.fecha_vencimiento - hoy).days

        if dias < 0:
            print("El producto está vencido")
            self.stock = 0

        return dias
    #Ejercicio 6
    def __str__(self):
        return f"Producto: {self.descripcion}, ID: {str(self.id_producto)}, Precio: ${str(self.precio)}, Stock: {str(self.stock)}"

    def __eq__(self, otro):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
    
    