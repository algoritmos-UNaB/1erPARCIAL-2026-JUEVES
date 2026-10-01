from datetime import date
class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def actualizar(self,descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock

    def dias_para_vencer(self):
        hoy = date.today()
        diferencia =(self.fecha_vencimiento - hoy).days
        if diferencia < 0:
            self.stock = 0
            return "Producto vencido. stock = 0"
        return  diferencia
    def marcar_stok_cero(self):
        self.stock = 0
    
    def __str__(self):
        return f"Producto: {self.descripcion}", ID: {self.id_producto}, Precio: ${self.precio:.2f}, Stock:{se.stock}"

    def __eq__(self, other):
        if isinstance(other, ProductoKwike):
            return self.id_producto == other.id_producto and self.descripcion == other.descripcion
        return False

        


