class Nodo(object):
    
    def __init__(self, dato=None, prox = None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)

        

    
def verLista(nodo):
    if nodo.dato == None:
        return
    else:
        while nodo:
            # muestra el dato
            print(nodo)
            # ahora nodo apunta a nodo.prox
            nodo = nodo.prox
        
        

if __name__ == "__main__":
    a = Nodo()
    b = Nodo("Datos nodo b")
    c = Nodo("datos nodo c",b)
    print("Revisando el nodo 'a'")
    print(verLista(a))
    print("")
    
    print("Revisando el nodo 'b'")
    print(verLista(b))
    print("")
    
    print("Revisando el nodo 'c'")
    print(verLista(c))
    print("")
    