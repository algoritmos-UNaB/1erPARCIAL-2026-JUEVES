from datetime import date
class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria=None):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
def actualizar(self, descripcion=None, precio=None, stock=None):
    if descripcion is not None:
            self.descripcion = descripcion
    if precio is not None:
            self.precio = precio
    if stock is not None:
            self.stock = stock
def dias_para_vencer(self):
        hoy = date.today()
    diferencia = (self.fecha_vencimiento - hoy).days
if diferencia < 0:
    print(f"¡Atención! El producto '{self.descripcion}' (ID {self.id_producto}) "
        f"ya venció hace {abs(diferencia)} día(s). Stock puesto en 0.")
            self.stock = 0
return diferencia
def __str__(self):
        return (f"[{self.id_producto}] {self.descripcion} - "
                f"${self.precio:.2f} - stock: {self.stock} - "
                f"vence: {self.fecha_vencimiento}")
def __eq__(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return (self.id_producto == otro.id_producto and
                self.descripcion == otro.descripcion)