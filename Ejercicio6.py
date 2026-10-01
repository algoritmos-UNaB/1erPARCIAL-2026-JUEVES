def __str__ ( self) : 
    return f"Producto : {self.descripcion} | ID : {self.id_producto} | precio : ${self.precio} | stock : {self.stock}"

def __eq__ (self, otro_producto) :
    return (self.id_producto == otro_producto.id_producto) and (self.descripcion == otro_producto.descripcion)