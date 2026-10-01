class KwikEMart:
    def __innit__(self):
        self.bebidas= []
        self.snacks= []
        self.conveniencia = []
    def agregar_producto(self,producto,seccion):
        if seccion == "bebidas":
            self.bebidas.append(producto)
        elif seccion == "snacks":
            self.snacks.append(producto)
        elif seccion == "Conveniencia":
            self.conveniencia.append(producto)
    def remover_producto(self,producto,seccion):
        if seccion=="bebidas":
            self.bebidas.remove(producto)
        elif seccion== "snacks":
            self.snacks.remove(producto)
        elif seccion== "Conveniencia":
            self.conveniencia.remove(producto)
    def actualizar_stock(self,producto,cantidad):
        producto.stock = cantidad
    def productos_por_vencer(self):
        cantidad= 0
        for producto in self.bebidas:
            if 0  <= producto.dias_para_vencer()  <=1:
                cantidad= cantidad + 1
        
        for producto in self.snacks:
            if 0  <= producto.dias_para_vencer()  <=1:
                cantidad= cantidad + 1
        
        for producto in self.conveniencia:
            if 0  <= producto.dias_para_vencer()  <=1:
                cantidad= cantidad + 1
        return cantidad
        