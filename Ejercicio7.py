from ejercicio_5 import productoKwikE
from datetime import date

class KwikEMart:
    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.golosinas = []

    def agregar_producto(self, producto: productoKwikE, seccion: str)
        if seccion == "Bebidas":
            self.bebidas.append(producto)
        elif seccion == "Snacks"
            self.snacks.append(producto)
        elif seccion == "Golosinas"
            self.golosinas.append(producto)
        else:
            print("seccion no válida. use 'Bebidas', 'Snacks', o 'Golosinas'.")

    def mostrar_producto(self)
        print("Productos en Bebidas")
        for producto in self.bebidas:
            print(producto)
        
        print("\nProductos en Snacks")
        for producto in self.snacks:
            print(producto)

        print("\nProductos en Golosinas")
        for producto in self.golosinas:
            print(producto)
    
    def eliminar_producto(self, producto: productoKwikE, seccion:str):
        if seccion == "Bebidas":
            if producto in self.bebidas
                self.bebidas.remove(producto)
            else:
                print("producto no encontrado")
        elif seccion == "Snacks"
            if producto in self.snacks
                self.snacks.remove(producto)
            else:
                print("producto no encontrado")
        elif seccion == "Golosinas"
            if producto in self.golosinas
                self.golosinas.remove(producto)
            else:
                print("producto no encontrado")
        else:
            print("seccion no válida. use 'Bebidas', 'Snacks', o 'Golosinas'.")

#Calcular cuántos productos expiran en las próximas 24 horas (con el metodo dias_restantes) y removerlos del inventario
    def eliminar_productos_vencidos(self):
        for seccion in [self.bebidas, self.snacks, self.golosinas]
            productos_a_eliminar = [ producto for producto in seccion[:] if producto.dias_restantes() <= 1]
            for producto in productos_a_eliminar:
                seccion.remove(producto)
                print(f'Producto {producto.descripcion} removido por estar vencido o expirar en las proximas 24 horas')
                
