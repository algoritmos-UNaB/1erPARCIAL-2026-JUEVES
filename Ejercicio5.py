class productoKwikE:
    def_init_(self, id_producto: int: str, fecha_vencimiento: date, precio: float, stock: int, categoria: str= "general"):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
    
def modificar_datos(self, descripcion: str=none, precio: float=none, stock: int=none):
    "modificar uno o varios datos del producto"
    if descripcion is not none:
        self.descripcion = descripcion
    if precio is not none:
        self.precio = precio
    if stock is not none:
        self.stock = stock

def calcular_dias_expiracion(self)
    "calcula los dias restantes hasta la fecha de vencimiento, si el producto esta expiado, informar al usuario y marcar el stock como 0"
    hoy = date.today()
    dias_restantes = (self.fecha_vencimiento - hoy). days

    if dias_restantes 0:
        self.stock = 0
        print("el producto 'self,descripcion' ha expirado, el stock a cambiado a 0")
        return dias_restantes
    else:
        print("faltan 'dias_restantes' para que se venza")
        return dias_restantes