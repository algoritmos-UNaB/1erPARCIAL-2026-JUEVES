from datetime import date

class KwikEMart:
    def __init__(self):
        # Representamos las secciones/pasillos con listas de productos
        self.pasillos = {
            "Bebidas": [],
            "Snacks": [],
            "Conveniencia": []
        }

    # Añadir un nuevo producto a un pasillo
    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)
        else:
            self.pasillos[pasillo] = [producto]

    # Remover un producto del inventario por su ID
    def remover_producto(self, id_producto):
        for lista in self.pasillos.values():
            for p in lista:
                if p.id_producto == id_producto:
                    lista.remove(p)
                    return True
        return False

    # Actualizar stock de un producto
    def actualizar_stock(self, id_producto, nuevo_stock):
        for lista in self.pasillos.values():
            for p in lista:
                if p.id_producto == id_producto:
                    p.stock = nuevo_stock
                    return True
        return False

    # Contar y remover productos que expiran en las próximas 24hs (<= 1 día)
    def remover_expirados_24hs(self):
        hoy = date.today()
        removidos = 0
        for pasillo, lista in self.pasillos.items():
            validos = []
            for p in lista:
                dias = (p.fecha_vencimiento - hoy).days
                if dias <= 1:
                    removidos += 1
                else:
                    validos.append(p)
            self.pasillos[pasillo] = validos
        return removidos