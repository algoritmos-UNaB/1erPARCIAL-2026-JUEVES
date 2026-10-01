import datetime

class ProductoKwikE:
    def __init__(self, nombre, descripcion, id_prod, fech_venc, precio, stock)
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_prod = id_prod
        self.fech_venc = fech_venc
        self.precio = precio
        self.stock = stock 
    
    def modif_descrip(self , new_descrip):
        self.descripcion = new_descrip
    def modif_precio(self , new_precio):
        self.precio = new_precio
    def modif_stock(self , new_stock):
        self.stock = new_stock
    def expiro(self):
        datetime.now() > self.fech_venc