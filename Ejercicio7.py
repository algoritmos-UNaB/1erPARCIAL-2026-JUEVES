from datetime import date 

#Defino clase KwikEMart 

class KwikEMart:
    def __init__(self):
        self.bebidas=[]
        self.snacks=[]
        self.conveniencia=[]

#Metodo para agregar un producto a un pasillo

def agregar_producto (self, producto, pasillo):
    if pasillo == "bebidas":
        self.bebidas.append(producto)
    elif pasillo == "snacks":
        self.snacks.append(producto)
    elif pasillo == "conveniencia":
        self.conveniencia.append(producto)
    else:
        print("Pasillo invalido. Use: bebidas, snacks o conveniencia.")

#Metodo para actualizar stock

def actualizar_stock(self,producto, nuevo_stock):
    producto.stock = nuevo_stock
    print(f"Stock actualizado: ahora hay {nuevo_stock} unidades de '{producto.descripcion}'.")

#Metodo para remover un producto del inventario

def remover_producto(self, id_producto):
    for pasillo in [self.bebidas, self.snacks, self.conveniencia]:
        for producto in pasillo:
            if producto.id_producto == id_producto:
                pasillo.remove(producto)
                print(f"Producto {producto.descripcion} fue removido del inventario.")
                return
    print("Producto no encontrado.")


#Metodo para ver los productos que vencen en menos de un 1 dia y desecharlos

def desechar_vencidos(self):
    hoy = date.today()
    contador = 0

    for pasillo in [self.bebidas,self.snacks, self.conveniencia]:
        for producto in pasillo[:]:
            if (producto.fecha_vencimiento - hoy).days <= 1:
                contador += 1
                self.remover_producto(producto.id_producto)
                print(f"Se desecha '{producto.descripcion}' por que vencera en las proximas 24 horas.")
    return contador 
