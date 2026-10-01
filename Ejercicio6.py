class ProductoKwikE:
      def __init__ (self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion 
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
      def __str__ (self):
        return f"Producto: {self.descripcion}, ID: {self.id_producto}, Precio: ${self.precio}, Stock: {self.stock}"
      def __eq__ (self, otro):
        return (self.id_producto == otro.id_producto and self.descripcion == otro.descripcion)
             