#importamos la clase date del módulo datetime para poder trabajar con fechas
from datetime import date

# Definimos la clase productoKwikE con sus atributos y métodos
class productoKwikE:
    def __init__(self, descripcion: str, id: int, vencimiento: date, precio: float, stock: int):
        self.descripcion = descripcion
        self.id = id
        self.vencimiento = vencimiento
        self.precio = precio
        self.stock = stock
    
    def dias_restantes(self):
# generamos la variable hoy con la fecha actual y calculamos los días restantes hasta la fecha de vencimiento
        hoy = date.today()
        dias_restantes = (self.vencimiento - hoy).days
# si los días restantes son menores a 0, significa que el producto está vencido y se actualiza el stock a 0
        if dias_restantes < 0:
            print("El producto está vencido, se actualizara el stock a 0")
            self.stock = 0
        return dias_restantes
    
    def actualizar_producto(self, descripcion: str = None, precio: float = None, stock: int = None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None:
            self.stock = stock