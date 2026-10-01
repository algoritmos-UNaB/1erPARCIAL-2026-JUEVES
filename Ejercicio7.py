from datetime import date


class KwikEMart:

    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

    def agregar_producto(self, producto, pasillo):
        if pasillo == "bebidas":
            self.bebidas.append(producto)

        elif pasillo == "snacks":
            self.snacks.append(producto)

        elif pasillo == "conveniencia":
            self.conveniencia.append(producto)

    def remover_producto(self, id_producto):
        for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
            for producto in pasillo:
                if producto.id_producto == id_producto:
                    pasillo.remove(producto)
                    return True

        return False

    def actualizar_stock(self, id_producto, nuevo_stock):
        for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
            for producto in pasillo:
                if producto.id_producto == id_producto:
                    producto.stock = nuevo_stock
                    return True

        return False

    def productos_por_vencer(self):
        hoy = date.today()
        cantidad = 0

        for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
            for producto in pasillo:
                dias = (producto.fecha_vencimiento - hoy).days

                if 0 <= dias <= 1:
                    cantidad += 1

        return cantidad