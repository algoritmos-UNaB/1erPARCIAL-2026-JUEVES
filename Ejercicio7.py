from datetime import date
class KwikEMart:
    def __init__(self, pasillos=None):
        nombres = pasillos or ["Bebidas", "Snacks", "Conveniencia"]
        self.pasillos = {nombre: [] for nombre in nombres}
def agregar_producto(self, pasillo, producto):
        if self.buscar_producto(producto.id_producto) is not None:
            raise ValueError(f"Ya existe un producto con ID {producto.id_producto}")
        self.pasillos.setdefault(pasillo, []).append(producto)

def remover_producto(self, id_producto):
        producto = self.buscar_producto(id_producto)
        if producto is None:
            return False
        for lista in self.pasillos.values():
            if producto in lista:
                lista.remove(producto)
        return True

def actualizar_stock(self, id_producto, nuevo_stock):
        producto = self.buscar_producto(id_producto)
        if producto is None:
            return False
        producto.modificar(stock=nuevo_stock)
        return True
def buscar_producto(self, id_producto):
        for lista in self.pasillos.values():
            for producto in lista:
                if producto.id_producto == id_producto:
                    return producto
        return None
def descartar_por_vencer(self):
        hoy = date.today()
        descartados = []
        for nombre, lista in self.pasillos.items():
            descartados += [p for p in lista if (p.fecha_vencimiento - hoy).days <= 1]
            self.pasillos[nombre] = [p for p in lista if (p.fecha_vencimiento - hoy).days > 1]
        return descartados

def __str__(self):
        lineas = []
        for nombre, lista in self.pasillos.items():
            lineas.append(f"{nombre}:")
            if lista:
                lineas += [f"  {p}" for p in lista]
            else:
                lineas.append("  (vacío)")
        return "\n".join(lineas)