class Node():
    def __init__(self, data = None):
        self.data = data
        self.izq = None
        self.der = None
        
    def __str__(self):
        return str(self.data)

class Arbol():
    def __init__(self, data = None):
        nodo = Node(data)
        self.raiz = nodo
    
    def agregar(self, data):
        new_nodo = Node(data)
        if self.raiz.data == None:
            self.raiz = new_nodo
        else:
            self.agregar_recursivo(self.raiz, new_nodo)
        
    def agregar_recursivo(self, nodo, new_nodo):
        if nodo.izq == None and nodo.der == None:
            if nodo.data < new_nodo.data:
                nodo.izq = new_nodo
            else:
                nodo.der = new_nodo
        else:
            if nodo.data > new_nodo.data:
                if nodo.der == None:
                    nodo.der = new_nodo
                else:
                    self.agregar_recursivo(nodo.der, new_nodo)
            elif nodo.data <= new_nodo.data:
                if nodo.izq == None:
                    nodo.izq = new_nodo
                else:
                    self.agregar_recursivo(nodo.izq, new_nodo)
