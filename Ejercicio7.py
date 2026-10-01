class KwikEMart:
    def __init__(self):
        self.pasillos = {
            "Bebidas": [], 
            "Snacks": [], 
            "Conveniencia": []
        }

    def agregar_producto(self, pasillo, producto):
        if pasillo in self.pasillos:
            self.pasillos[pasillo].append(producto)

    def remover_producto(self, id_producto):
        for pasillo, lista in self.pasillos.items():
            self.pasillos[pasillo] = [p for p in lista if p.id_producto != id_producto]

    def desechar_expirados_24hs(self):
        for pasillo, lista in self.pasillos.items():
            self.pasillos[pasillo] = [p for p in lista if p.dias_para_expirar() > 1]