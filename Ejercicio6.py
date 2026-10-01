from datetime import datetime, timedelta
from ejercicio5 import ProductoKwikE

class ProductoKwikE_(ProductoKwikE):
    def __str__(self):
        estado = 'Vencido' if datetime.now() > self.fecha_vencimiento else f'Vence en {self.dias_vencimiento()}'
        return f'{self.id_producto} | {self.descripcion} | Precio: {self.precio} | Stock: {self.stock} | {estado}'
    def __eq__(self, otro):
        if type(otro) != type(self):
            return False
        return self.id_producto == otro.id_producto and self.descripcion == otro.descripcion
