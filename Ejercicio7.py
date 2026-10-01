from datetime import date
class ProductoKwikE:
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock, categoria=""):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def actualizar(self, nueva_desc="", nuevo_precio=0, nuevo_stock=-1):
        if nueva_desc != "":
            self.descripcion = nueva_desc
        if nuevo_precio != 0:
            self.precio = nuevo_precio
        if nuevo_stock != -1:
            self.stock = nuevo_stock
            
    def __str__(self):
        return f"[{self.id_producto}] {self.descripcion} - ${self.precio} - stock: {self.stock} - vence: {self.fecha_vencimiento}"
class KwikEMart:
    def __init__(self, pasillos=["Bebidas", "Snacks", "Conveniencia"]):
        self.pasillos = {}
        for nombre in pasillos:
            self.pasillos[nombre] = []
def buscar_producto(self, id_producto):
        for lista in self.pasillos.values():
            for producto in lista:
                if producto.id_producto == id_producto:
                    return producto
        return None
def agregar_producto(self, pasillo, producto):
        if self.buscar_producto(producto.id_producto) != None:
            print("Ya existe un producto con ID " + str(producto.id_producto))
            return
        if pasillo not in self.pasillos:
            self.pasillos[pasillo] = []
            
        self.pasillos[pasillo].append(producto)
 def remover_producto(self, id_producto):
        for pasillo, lista in self.pasillos.items():
            for producto in lista:
                if producto.id_producto == id_producto:
                    lista.remove(producto)
                    print(f"Se removio {producto.descripcion} del inventario (pasillo {pasillo})")
                    return True
        print("No se encontro el producto para remover")
        return False
def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_producto(id_producto)
        if producto != None:
            producto.actualizar(nuevo_stock=nuevo_stock)
            print(f"Stock de {producto.descripcion} actualizado a {nuevo_stock}")
            return True
        print("Producto no encontrado")
        return False
def descartar_proximos_a_vencer(self):
        hoy = date.today()
        descartados = []
        
        for nombre, lista in self.pasillos.items():
            conservados = []
            for producto in lista:
                tiempo = producto.fecha_vencimiento - hoy
                if tiempo.days <= 1:
                    descartados.append(producto)
                else:
                    conservados.append(producto)
            self.pasillos[nombre] = conservados

        for p in descartados:
            print(f"Apu desecho: {p.descripcion} (vence {p.fecha_vencimiento})")
            
        print(f"Total desechados: {len(descartados)}")
        return len(descartados)

    def __str__(self):
        texto = "--- Inventario Kwik-E-Mart ---\n"
        for nombre, lista in self.pasillos.items():
            texto = texto + nombre + ":\n"
            if len(lista) == 0:
                texto = texto + "  (vacio)\n"
            else:
                for p in lista:
                    texto = texto + "  " + str(p) + "\n"
        return texto