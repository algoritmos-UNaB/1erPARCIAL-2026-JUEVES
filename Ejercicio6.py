#La Etiqueta de los Productos del Kwik-E-Mart 

class ProductoKwikE:
    def __init__(self, desc,id_p, fecha,precio, stock):
        self.descripcion=desc
        self.id_producto=id_p
        self.fecha_vencimiento=fecha
        self.precio=precio
        self.stock=stock
#pongo solo el constructor para recordar el nombre de los self


    def __str__(self):
        return (f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio} | Stock:{self.stock}")

    def __eq__(self,producto_2):
        return (self.id_producto == producto_2.id_producto and self.descripcion==producto_2.descripcion)
    