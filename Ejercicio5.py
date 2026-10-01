#El Inventario del Kwik-E-Mart

from datetime import date

class ProductoKwikE:
    def __init__(self, desc,id_p, fecha,precio, stock):
        self.descripcion=desc
        self.id_producto=id_p
        self.fecha_vencimiento=fecha
        self.precio=precio
        self.stock=stock
    
    def Cambiar (self,descrip=None,precio=None,stock=None):
        if descrip!=None:
            self.descripcion=descrip
        if precio!=None:
            self.precio=precio
        if stock!=None:
            self.stock=stock
        return

    def Dias_expiro (self,dia):
        hoy = date.today()
        dif_dias = self.fecha_vencimiento - hoy
        dias_restantes = dif_dias.days
        if dias_restantes <0:
            print (f"el producto {self.descripcion} expiro. El stock vale 0.")
            self.stock = 0
        else:
            print(f"el producto {self.descripcion} expira en {dias_restantes} dias.")
        return dias_restantes


