from datetime import datetime, timedelta

class ProductoKwikE:
    def __init__(self,descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento 
        self.precio = precio
        self.stock = stock
        self.verificar_vencimiento()
    def cambiar(self, descripcion = None, fecha_vencimiento = None, precio = None, stock = None):
        if descripcion is not None:
            self.descripcion = descripcion
        if fecha_vencimiento is not None:
            self.fecha_vencimiento = fecha_vencimiento
        if precio is not None: 
            self.precio = precio
        if stock is not None:
            self.stock = stock
        self.verificar_vencimiento()
    def verificar_vencimiento(self):
        if datetime.now() > self.fecha_vencimiento:
            print(f"El producto {self.descripcion} {self.id_producto} esta vencido.")
            self.stock = 0
            return True
        return False
    def dias_vencimiento(self):
            diferencia = self.fecha_vencimiento - datetime.now()
            return diferencia.days