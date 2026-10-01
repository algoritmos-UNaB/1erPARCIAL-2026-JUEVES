def __str__(self):
    return f"Producto: {self.nombre} - ID: {self.id_prod} - Precio:{self.precio} - Stock:{self.stock}"

def __eq__(self , otro):
    return self.descripcion == otro.descripcion and self.id_prod == otro.id_prod