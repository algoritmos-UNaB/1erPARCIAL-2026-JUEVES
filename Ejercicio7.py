from datetime import date, timedelta
class KwikEMart:
    def __init__(self, nombre="Kwik-E-Mart", pasillos=("Bebidas", "Snacks", "Conveniencia")):
        self.nombre = nombre
        self.pasillos = {p: [] for p in pasillos}

    def _todos(self):
        return [prod for list in self.pasillos.values() for prod in list]

    def buscar_por_id(self, id_producto):
        for prod in self._todos():
            if prod.id_producto = id_producto:
                return prod
        return None

    def agregar_producto(self, producto, pasillo="Conveniencia"):
        if self.buscar_por_id(producto.id_producto):
            print(f"El ID {producto.id_producto} ya existe.")
            return None
        producto.pasillo = pasillo
        self.pasillos.setdefault(pasillo, []).append(producto)
        print(f"'{producto.descripcion}' agregado a '{pasillo}'.")
        return producto

    def remover_producto(self, id_producto):
        prod = self.buscar_por_id(id_producto)
        if prod:
            self.pasillos[prod.pasillo].remove(prod)
            print(f"'{prod.descripcion}' removido.")
        else:
            print(f"No existe el ID {id_producto}.")
        return prod

    def actualizar_stock(self, id_producto, cantidad):
        prod = self.buscar_por_id(id_producto)
        if not prod:
            print(f"No existe el ID {id_producto}.")
            return None
        if prod.stock + cantidad < 0:
            print("Stock insuficiente.")
            return None
        prod.stock += cantidad
        print(f"Stock de '{prod.descripcion}': {prod.stock}")
        return prod.stock

    def apu_desecha_caducados(self, horas=24):
        limite = date.today() + timedelta(hours=horas)
        caducados = [p for p in self._todos() if p.stock > 0 and p.fecha_vencimiento <= limite.date()]
        for prod in caducados:
            prod.stock = 0
            self.pasillos[prod.pasillo].remove(prod)
            print(f"Desecha '{prod.descripcion}'.")
        if not caducados:
            print("Nada para desechar")
        return caducados

    def total_productos(self):
        return len(self._todos())

    def valor_inventario(self):
        return sum(p.precio * p.stock for p in self._todos())

    def __str__(self):
        texto = f"= {self.nombre}"
        for pasillo, list in self.pasillos.items():
            texto += f"\n[{pasillo}]"
            for prod in list:
                texto += f"\n   {prod}"
        return texto + f"\nTotal: {self.total_productos()}, Valor: ${self.valor_inventario():.2f}"