#en este codigo se envian en conjunto el punto 5 y 6
from datetime import date, timedelta
class ProductoKwikE():
  def __init__(self, id_producto: str, fecha_venc: date, precio: float, stock: int):
    self.id_producto = id_producto
    self.fecha_venc = fecha_venc
    self.precio = precio
    self.stock = stock
  
  def calcular_caducidad(self):
    Hoy = date.today() 
    caduca_en = self.fecha_venc - Hoy
    if caduca_en < timedelta(0):
      print("el producto expiro")
    return caduca_en 
  
  def actualizar_datos(self, stock_restante, precio_nuevo):
    self.stock= stock_restante
    self.precio= precio_nuevo
  def __str__(self):
    return f"el produco1 tiene: ID: {self.id_producto}, vence el{self.fecha_venc}, cuesta {self.precio} y quedan {self.stock} unidades"
  def __eq__(self, distinto):
    return self.id_producto == distinto.id_producto
producto1 = ProductoKwikE("123", date(2026, 10, 9), 1499.99, 26)
producto2 = ProductoKwikE("123", date(2027,3,12), 300.05, 40 )
print(producto1.calcular_caducidad())
print(producto1 == producto2)
