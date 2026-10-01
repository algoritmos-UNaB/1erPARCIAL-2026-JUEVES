class productokwike:
    def __init__ (self, descripcion, id producto, fechavencimiento, precio, stock)
    

self.descripcion = descripcion
self.id_producto = id_producto
self.fecha_vencimiento = fecha_vencimiento
self.precio = precio
self.stock = stock

def actualizar_datos (self, precio=None, stock=None):
    if precio is not None:
        self.precio = precio
    if stock is not None:
        self.stock = stock


def dias_expira(self):
    if dias_restantes < 0:
        print(f"El producto '{self.descripcion}' ya expiró.")
            self.stock = 0

    else print(f"Al producto '{self.descripcion}' le quedan {dias_restantes} días.")

    return dias_restantes         

def __str__(self):
    return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"

def __eq__(self, otro): 
    return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion


