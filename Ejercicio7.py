from Ejercicio5 import ProductoKwikE

class KwikEMart:
    def __init__(self):
        self.sectorBebidas = []
        self.sectorSnacks = []
        self.sectorConveniencia = []

    def buscar_ID(self, id_producto):
        for producto in self.sectorBebidas:
            if producto.id_producto == id_producto:
                return "Bebidas", producto
        for producto in self.sectorSnacks:
            if producto.id_producto == id_producto:
                return "Snacks", producto
        for producto in self.sectorConveniencia:
            if producto.id_producto == id_producto:
                return "Conveniencia", producto

        return None, None

    def agregar_producto(self, pasillo:str, producto):
        if pasillo == "Bebidas":
            self.sectorBebidas.append(producto)
            return

        if pasillo == "Snacks":
            self.sectorSnacks.append(producto)
            return
        
        if pasillo == "Conveniencia":
            self.sectorConveniencia.append(producto)
            return
        print("No existe ese pasillo.")
        

    def remover_expirar(self, fecha_actual):
        cantidad=0

        for producto in self.sectorBebidas[:]:
            dias_restantes = (producto.fecha_vencimiento - fecha_actual).days
            if dias_restantes <= 1:
                self.sectorBebidas.remove(producto)
                cantidad += 1
        for producto in self.sectorSnacks[:]:
            dias_restantes = (producto.fecha_vencimiento - fecha_actual).days
            if dias_restantes <= 1:
                self.sectorSnacks.remove(producto)
                cantidad += 1
        for producto in self.sectorConveniencia[:]:
            dias_restantes = (producto.fecha_vencimiento - fecha_actual).days
            if dias_restantes <= 1:
                self.sectorConveniencia.remove(producto)
                cantidad += 1
        return cantidad
        
    

    