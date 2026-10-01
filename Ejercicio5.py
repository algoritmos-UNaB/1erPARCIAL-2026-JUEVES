from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock)
    self.descripcion = descripcion (str)
    self.id_producto = id_producto (int)
    self.fecha_vencimiento = fecha_vencimiento (date)
    self.precio = precio (float)
    self.stock = stock (int)

    def cambiar_datos(descripcion, precio, stock,):
        descripcion=None
        Precio=None
        Stock=None

        if descripcion is not None:
            self.descripcion = descripcion

        if precio is not None:
            self.precio = precio

        if stock is not None:
            self.stock = stock

    def vencimiento(self):
        hoy = date.today()
        dias = (self.fecha_vencimiento-hoy)

        if dias < 0:
            print("El producto esta vencido")
            self.stock = -1

