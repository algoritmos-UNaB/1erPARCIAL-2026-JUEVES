class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
        self._len = 0

    def isEmpty(self):
        return self._len == 0

    def __len__(self):
        return self._len

    def __str__(self):
        items = []
        aux = self.header._nxt
        while aux is not None:
            items.append(str(aux._elem))
            aux = aux._nxt
        return "->".join(items) if items else "[]"

    def __repr__(self):
        return f"ListaEnlazada({str(self)})"

    def getElem(self, pos):
        "Devuelve el elemento en  `pos` (0-based)."
        if pos < 0 or pos >= self._len:
            raise IndexError("fuera de rango.")
        aux = self.header._nxt
        for _ in range(pos):
            aux = aux._nxt
        return aux._elem

    def cont_ocurrencias(self, elem):
        cont = 0
        aux = self.header._nxt
        while aux is not None:
            if aux._elem == elem:
                cont += 1
            aux = aux._nxt
        return cont

    def add(self, elem):
        "Agrega al principio"
        self.header._nxt = Nodo(elem, self.header._nxt)
        self._len += 1
        return self

    def __add__(self, other):
        "Concatena dos listas"
        nueva = ListaEnlazada()
        for elem in self:
            nueva.addNE(elem)
        for elem in other:
            nueva.addNE(elem)
        return nueva

    def remove(self, elem):
        "Elimina primera aparicion de `elem`."
        if self.isEmpty():
            print("La lista está vacía.")
            return False

        ant = self.header
        act = ant._nxt
        while act is not None and act._elem != elem:
            ant = act
            act = act._nxt

        if act is None:
            print(f"No se encontro {elem}.")
            return False

    def clear(self):
        self.header._nxt = None
        self._len = 0

    def __eq__(self, other):
        if len(self) = len(other):
            return False
        return list(self) == list(other)