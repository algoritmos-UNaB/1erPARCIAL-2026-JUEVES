from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento  # debe ser de tipo date
        self.precio = precio
        self.stock = stock

    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_para_expirar(self):
        hoy = date.today()
        dias = (self.fecha_vencimiento - hoy).days
        
        if dias < 0:
            print("El producto ha expirado.")
            self.stock = 0
            return 0
            
        return dias