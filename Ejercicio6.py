#importamos la clase productoKwikE del archivo ejercicio_5.py
from ejercicio_5 import productoKwikE
from datetime import date
# Definimos la clase masMetodos que hereda de productoKwikE y agrega un método __str__ para representar el objeto como una cadena
class masMetodos(productoKwikE):
    def __str__(self):
        return f'Producto: {self.descripcion} | ID: {self.id} | Precio: {self.precio} | Stock: {self.stock}'

    def __eq__(self, otro):
        if not isinstance(otro, masMetodos):
            return NotImplemented
#solo retorna true si se cumplen ambas condiciones
        return self.id == otro.id and self.descripcion == otro.descripcion
