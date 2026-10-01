class productoKwikE:
    def_init_(self, id_producto:int, descripcion:str, precio: float, stock:int, horas_para_es¡xpirar: float):
        self.id_producto = id_producto
        self.descripcion= id_descripcion
        self.precio = id.precio
        self.stock = stock

    def_str_(self)
        return "producto: [self.producto]|ID: [self.id_producto]| precio: [self.precio]| stock:[self.stock] "

    def_eq_(self, otro):
        if not isinstance (otro, productoKwikeE):
            return false 
        return self.id_producto == otro.id_producto and self. descripcion == otro.descripcion

