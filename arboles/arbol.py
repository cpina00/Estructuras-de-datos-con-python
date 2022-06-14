from re import A


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

    def __str__(self):
        return self.mostrar()
    
    def mostrar(self, ascendente = False):
        if ascendente:
            return "ascendente: " + self.mostrar_ascendente(self.raiz)
        else:
            return "descendente: " + self.mostrar_descendente(self.raiz)
            
    
    def mostrar_descendente(self, nodo):
        
        if nodo.data != None and nodo.der != None and nodo.izq != None:
            return str(self.mostrar_descendente(nodo.izq)) +"->" + str(nodo) +"->"+ str(self.mostrar_descendente(nodo.der))
        elif nodo.data != None and nodo.izq != None:
            return str(self.mostrar_descendente(nodo.izq)) +"->"+ str(nodo)
        elif nodo.data != None and nodo.der != None:
            return str(nodo) +"->"+ str(self.mostrar_descendente(nodo.der))
        elif nodo.data != None:
            return str(nodo)
    
    def mostrar_ascendente(self, nodo):
        if nodo.data != None and nodo.der != None and nodo.izq != None:
            return str(self.mostrar_ascendente(nodo.der)) +"->" + str(nodo) +"->"+ str(self.mostrar_ascendente(nodo.izq))
        elif nodo.data != None and nodo.der != None:
            return  str(self.mostrar_ascendente(nodo.der)) +"->"+  str(nodo)
        elif nodo.data != None and nodo.izq != None:
            return str(nodo) +"->"+ str(self.mostrar_ascendente(nodo.izq))
        elif nodo.data != None:
            return str(nodo)
        
    """
    Función para buscar un elemento (devuelve True o False)
Función para contar cuantos elementos tenemos en el árbol.
Función que cuenta cuantos niveles tiene el árbol.
"""
    def encontrar(self, valor):
        if self.raiz == None:
            return False
        else:
            return self._encontrar(self.raiz, valor)
        
    def _encontrar(self, nodo, valor):
        if nodo.data != None:
            if nodo.data == valor:
                return True
            elif nodo.data > valor:
                if nodo.der!=None:
                    return self._encontrar(nodo.der, valor)
                else:
                    return False
            else:
                if nodo.izq != None:
                    return self._encontrar(nodo.izq, valor)
                else:
                    return False
        else:
            return False
        
    
    
    

if __name__=="__main__":
    arbol_a = Arbol(5)
    arbol_a.agregar(10)
    arbol_a.agregar(4)
    arbol_a.agregar(11)
    arbol_a.agregar(8)
    arbol_a.agregar(4)
    arbol_a.agregar(5)
    arbol_a.agregar(3)
    arbol_a.agregar(30)
    arbol_a.agregar(9)
    arbol_a.agregar(8)
    arbol_a.agregar(4)
    arbol_a.agregar(2)
    arbol_a.agregar(15)
    
    #print(f"El arbol se ve: {arbol_a.mostrar()}")
    #print(f"El arbol se ve: {arbol_a.mostrar(True)}")
    print(arbol_a.encontrar(15))
    print(arbol_a.encontrar(16))
    
    
    
    
    
    
        
   