# Ejercicio 5 #
from datetime import date

class ProductoKwikE:
    def __init__(self, descripcion:str, id_producto:int, fecha_vencimiento:date, precio:float, stock:int):

        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
    
    def cambiar_stock(self, nuevo_stock):
        self.stock = nuevo_stock
    
    
    def dias_vencimiento(self, fecha_actual:date):
        fecha_expiracion = (self.fecha_vencimiento - fecha_actual).days

        if fecha_expiracion < 0:
            print("El producto expiró.")
            self.stock = 0
            return 0
        return fecha_expiracion
    


# EJERCICIO 6 #

    def __str__(self):
        return f"producto: {self.descripcion}, ID: {self.id_producto}, Precio: {self.precio}, Stock: {self.stock}"


    def __eq__(self, otro):
        if self.id_producto != otro.id_producto:
            return False

        if self.descripcion!= otro.descripcion:
            return False
            
        return True
        





   


