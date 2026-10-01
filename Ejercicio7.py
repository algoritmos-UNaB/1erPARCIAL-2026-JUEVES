class KwikEMart(): 
  def __init__(self):
    self.secciones = {
        "bebidas": [],
        "snaks": [],
        "conveniencia": []
    }
  
  def agregar_productos(self, productos, seccion):
    self.secciones[seccion].append(productos)
  
  def remover_producto(self, producto, seccion):
        self.secciones[seccion].remove(producto)

  def actualizar_stock(self, id_producto, seccion, nuevo_stock):
    for producto in self.secciones[seccion]:
        if producto.id_producto == id_producto:
            producto.stock = nuevo_stock
            return 
  def remover_caducados(self):
    hoy = date.today()

    for seccion in self.secciones:
        for producto in self.secciones[seccion].copy():
            if producto.fecha_venc < hoy:
                self.secciones[seccion].remove(producto)