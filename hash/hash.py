class Hash:
    def __init__(self, largo=10):
        self.largo = largo
        self.tabla = [None]*self.largo
        self.len = 0
    def agregar(self, elemento):
        indice = self._hash_funcion(elemento)
        if self.tabla[indice] == None:
            variable = [elemento]
            self.tabla[indice] = variable.copy()
        else:
            self.tabla[indice].append(elemento)
        self.len += 1
      
    def _hash_funcion(self, elemento):
        if type(elemento) is str:
          indice=len(elemento)
          indice = indice % self.largo
          return indice
        else:  
          indice = elemento % self.largo
          indice = round(indice)
          return indice
        
        
    def buscar(self, elemento):
        indice = self._hash_funcion(elemento)
        if self.tabla[indice] == elemento:
            return True
        else:
            return False
        
    def __len__(self):
        return self.len

    def __str__(self):
      return str(self.tabla)
        
        
        
        
if __name__ == "__main__":
    variable_hash = Hash()
    variable_hash.agregar(153)
    variable_hash.agregar(253)
    variable_hash.agregar(155)
    variable_hash.agregar("hola")
    
    print("Los elementos en variable_hash son:",len(variable_hash))

    print("Toda la tabla es:")
    print(variable_hash)
