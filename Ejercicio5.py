from datetime import date

class ProductoKwikE:
    def __init__ (
        self, descricion=str, id_producto=int , fecha_vencimiento=date, precio=float, stock=int
    ): 
    self.descricion = descricion
    self.id_producto = id_producto
    self.fecha_vencimiento = fecha_vencimiento
    self.precio = precio
    self.stock = stock

    def actualizar_produ (
        self, descricion=None, precio=None, stock=None 
    )
    if descricion is not None: 
        self.descricion  = descricion  

    if precio is not None: 
        self.precio  = precio  

    if stock is not None: 
        self.stock  = stock

    def vencimiento (self):
        dias (self.fecha_vencimiento - date.today ()).days

        if dias < 0:
            print("Producto vencido")
            self.stock = 0

        return dias  
