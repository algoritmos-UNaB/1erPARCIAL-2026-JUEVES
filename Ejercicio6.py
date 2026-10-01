## Ejercicio 6: La Etiqueta de los Productos del Kwik-E-Mart (Sobrecarga de Métodos)

from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion: str, id_producto: int, fecha_vencimiento: date, precio: float, stock: int):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
    def actualizar_datos(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is no None:
            self.stock = stock
    def dias_expira():
        hoy = date.today()
        dias_restantes = (self.fecha_vencimient - hoy).days
        if dias_restantes < 0:
            self.stock = 0
            print(f"El producto '{self.descripcion}' expiro.")
            return dias_restantes
        return dias_restantes
    def __str__(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"
    def __eq__(self):
        if not isinstance(otro, ProductoKwikE):
            return False
        return sef.id_producto == otro.id_producto and self.descripcion == oreo.descripcion
