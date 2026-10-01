# Metodos a incluir dentro de la clase ProductoKwikE

def __str__(self):
    return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock: {self.stock}"

def __eq__(self, otro):
    if isinstance(otro, ProductoKwikE):
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
    return False