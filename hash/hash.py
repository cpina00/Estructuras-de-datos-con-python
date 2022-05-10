import numpy as np

class Hash:
    def __init__(self, largo=100):
        self.largo = largo
        self.tabla = np.zeros(self.largo)
        self.len = 0
    def agregar(self, elemento):
        indice = self._hash_funcion(elemento)
        if self.tabla[indice] == 0:
            self.tabla[indice] = elemento
        else:
            self.tabla[indice+1] = elemento
        self.len += 1
    def _hash_funcion(self, elemento):
        indice = elemento % self.largo
        return indice
        
    def buscar(self, elemento):
        indice = self._hash_funcion(elemento)
        if self.tabla[indice] == elemento:
            return True
        if self.tabla[indice+1] == elemento:
            return True
        else:
            return False
        
    def __len__(self):
        return self.len
        
        
        
        
if __name__ == "__main__":
    variable_hash = Hash()
    variable_hash.agregar("153")
    variable_hash.agregar(53)
    
    print("Los elementos en variable_hash son:",len(variable_hash))
    if variable_hash.buscar(142):
        print("Si existe")
    else:
        print("No existe")
    if variable_hash.buscar(153):
        print("Si existe")
    else:
        print("No existe")
        
    if variable_hash.buscar(53):
        print("Si existe")
    else:
        print("No existe")
