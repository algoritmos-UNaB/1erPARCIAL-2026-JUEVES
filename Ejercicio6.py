##__str__: Para representar el producto de forma legible (ej: "Producto: Donuts Glaseadas | ID: 123 | Precio: $1.50 | Stock: 50").
## __eq__: Para comparar si dos productos son iguales basándose en su id_producto y descripcion.

from Ejercicio5 import ProductoKwikE: 

class ProductoKwikE(ProductoKwikE):
    def __str__ (self):
        return (
            f"Procduto: {self.descricion} | "
            f"ID: {self.id_producto} | "
            f"Precio: ${self.precio} | "
            f"Stock: {self.stock} | "
        )

    def __eq__ (self, otro):
        return (
            sel.id_producto == otro.id_producto and self.descricion == otro.descricion
        )
