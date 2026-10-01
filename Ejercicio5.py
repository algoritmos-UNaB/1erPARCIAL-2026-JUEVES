import datetime
class ProductoKwikE:
    def init(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria=None):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
def actualizar(self, **cambios):
        atributos_permitidos = ("descripcion", "precio", "stock")
    for clave, valor in cambios.items():
        if clave in atributos_permitidos:
                setattr(self, clave, valor)

def esta_vencido(self):
        return self.fecha_vencimiento < datetime.date.today()
def dias_para_vencer(self):
        dias = (self.fecha_vencimiento - datetime.date.today()).days

if self.esta_vencido():
            print(f"El producto {self.id_producto} - {self.descripcion} está vencido.")
            self.stock = 0
return dias
def str(self):
        return f"{self.id_producto} | {self.descripcion} | ${self.precio} | stock: {self.stock}"
def eq(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return (self.id_producto == otro.id_producto and
                self.descripcion == otro.descripcion)