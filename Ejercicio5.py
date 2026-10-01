from datetime import date

class ProductoKwikE:
    def __init__ ( self, descrpcion , id_producto , fecha_vencimiento , precio , stock , categoria) :
        self.descrpcion = str (descrpcion)
        self.id_producto = int (id_producto)
        self.fecha_vencimiento = (fecha_vencimiento)
        self.precio = float (precio)
        self.stock = int (stock)
        self.categoria = str ( categoria)

    def actualizar_datos ( self , descrpcion = None , precio = None , stock = None , categoria = None ) :
        if descrpcion is not None :
            self.descrpcion = str ( descrpcion)
        if precio is not None : 
            self.precio = float (precio)
        if stock is not None : 
            self.stock = int ( stock )
        if categoria is not None :
            self.categoria = str (categoria)    

    def dias_para_experirar (self) : # calcula los dias restantes para el vencimiento
        hoy = date.today()   
        dias_restantes = (self.fecha_vencimiento - hoy)

        if dias_restantes < 0 : 
            print ( f" el producto esta vencido")
            self.stock = 0
            return 0
        return dias_restantes            

