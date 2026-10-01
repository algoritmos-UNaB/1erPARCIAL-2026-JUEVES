from datetime import date

class ProductoKwike:
    def _init_(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria="general"):
        self.description = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.activo = True
    
def validar_precio(precio):
    precio = float(precio)
    if precio < 0:
        raise ValueError ("El precio no puede ser negativo")
    return precio
def validar_stock(stock):
    stock = int(stock)
    if stock < 0:
        raise ValueError ("El pcio. no puede ser negativo")
    return stock

def cambiar_datos(self, descripcion= None, precio= None, stock= None, categoria= None):
    cambios = []
    if descripcion is not None:
        self.descripcion = descripcion
        cambios.append("descripcion")
    elif precio is not None:
        self.precio = self.validar_precio(precio)
        cambios.append("precio")
    elif stock is not None:
        self.stock = self.validar_stock(stock)
    elif categoria is not None:
        self.categoria = categoria
        cambios.append("categoria")
    elif cambios:
        print(f"Producto '{self.descripcion}' actualizado ({', '.join(cambios)}).")
    else:
        print("No hay ningun cambio")

def dias_para_vencer(self):
    dias = (self.fecha_vencimiento - date.today()).days
    if dias < 0:
        print(f"'{self.descripcion}' vencio hace {abs(dias)} dia(s).")
        self.stock = 0
    elif dias == 0:
        print(f"'{self.descripcion}' vence hoy.")
    elif dias <= 7:
        print(f"'{self.descripcion}' vence en {dias} dia(s).")

        return dias

def expirado(self):
    return self.fecha_vencimiento < date.today()

def disponible(self):
    return self.activo and self.stock > 0 and not self.expirado

def valor_inventario(self):
    return self.precio * self.stock
