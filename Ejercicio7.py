class KwikEMart :
    def __init__ (self) #uso diccionario para manejar las listas (pasillos)
        self.pasillos = {"bebidas" : [], "snacks" : [], "conveniencia", []}

    def agregar_productos ( self, nombre_pasillo, producto) : 
        if nombre_pasillo  not in self.pasillos :
            self.pasillos[nombre_pasillo] = []

        self.pasillos[nombre_pasillo].append(producto)  

    def buscar_producto ( self, id_producto) :
        for nombre_pasillo, lista_productos in self.pasillos.items() :
            for producto in lista_productos : 
                if producto.id_producto == id_producto :
                    return producto , nombre_pasillo 

    def remover_producto (self, id_producto) : #remueve un producto usando la id
        producto, nombre_pasillo = self.buscar_producto ( id_producto)
        if producto is not None :
            self.pasillos [nombre_pasillo].remove(producto)

    def actualizar_stock (self, id_producto, nuevo_stock) :
        producto = self.buscar_producto(id_producto)

        if producto is not None :
            producto.actualizar_datos(stock = nuevo_stock)  

    