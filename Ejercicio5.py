#Defino class ProductoKwikE

class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion                                 #string
        self.id_producto = id_producto                                 #integer                         
        self.fecha_vencimiento = fecha_vencimiento                     #date
        self.precio = precio                                           #float
        self.stock = stock                                             #integer
#metodo para cambiar descripcion
    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
#metodo para cambiar precio
    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
#metodo para modificar stock
    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock 

#metodo para calcular en cuantos dias vence un producto
    def dias_restantes(self):
        hoy = date.today()
        diferencia = (self.fecha_vencimiento - hoy).days

        if diferencia < 0:
            print (f"El producto '{self.descripcion}' ha expirado.")
            self.stock = 0
            return 0 
        return diferencia

#metodo general para cambiar varios datos a la vez
    def actualizar(self, descripcion=None, precio=None, stock=None):
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if stock is not None: 
            self.stock = stock        
    