#La Gestion del Kwik-E-Mart

from datetime import date


class KwikEMart:
    def __init__(self):
        self.pasillos = {"Bebidas": [], "Snacks": [], "Conveniencias": []}

    def agregar_pasillo(self, n_pasillo: str):
        try:
            if n_pasillo in self.pasillos:
                raise ValueError(f"El pasillo {n_pasillo} ya existe.")    
            self.pasillos[n_pasillo] = []       
        except ValueError as error:
            print(f"{error}")
    def agregar_producto(self, pasillo: str, producto):
        try:
            self.pasillos[pasillo].append(producto)
            print(f"{producto.descripcion} agregado al pasillo {pasillo}")
        except KeyError:
            print(f"el pasillo {pasillo} no existe.")
        except AttributeError:
            print("el objeto no es un producto valido")
    def remover_producto(self, pasillo: str, producto):
        try:
            self.pasillos[pasillo].remove(producto)
            print(f"producto removido del pasillo {pasillo}")
        except KeyError:
            print(f"el pasillo {pasillo} no existe.")
        except ValueError:
            print("el producto no se encuentra en el pasillo.")
    
    def verificar_vencimientos(self):
        hoy = date.today()
        contador_desechados = 0
        for pasillo, productos in self.pasillos.items():
            for producto in productos[:]:
            diferencia = producto.fecha_vencimiento - hoy
            if diferencia.days <= 1:
                print(f"Desechando {producto.descripcion} del pasillo")
                self.remover_producto(pasillo, producto)
                contador_desechados += 1
        return contador_desechados


    
   