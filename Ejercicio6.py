#sobrecargue en el ejercicio 5 lo siguiente:
def eq(self, otro):
        if not isinstance(otro, ProductoKwikE):
            return False
        return (self.id_producto == otro.id_producto and
                self.descripcion == otro.descripcion)