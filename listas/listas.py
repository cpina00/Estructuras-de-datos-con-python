from msilib.schema import Error


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None
        self._len = 0

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
        self._len +=1
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
        else:
            n = self.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        self._len +=1
    
    def insert_to_index(self,index,data):
        if self.start_node is None:
            if index == 0:
                self.insert_at_start(data)
            else:
                print("Error") # Añadir una excepción correspondiente.
        else:
            if index <= self._len:
                if index == self._len:
                    self.insert_at_end(data)
                else:
                    n = self.start_node
                    contador = 1
                    while contador < index:
                        n = n.ref
                        contador +=1
                    new_node = Node(data)
                    new_node.ref = n.ref
                    n.ref = new_node
                    self._len +=1
                    
                    
                
            
            
    
    def remove_to_begin(self):
        if self.start_node is not None:
            self.start_node = self.start_node.ref
            self._len -=1
    
    def remove_to_end(self):
        if self.start_node is not None:
            if self._len == 1:
                self.start_node = None
                self._len -=1
            else:
                n = self.start_node
                contador = 1
                while contador < self._len-1:
                    n = n.ref
                    contador +=1
                n.ref = None
                self._len -=1
    
    def remove_to_index(self,index):
        pass
      
    ### Estos 4 métodos son esenciales para que funcionen los test.
    # NO TOCAR... 

    def __str__(self):
        """ this method is for print(), return the contain of list. """
        if self.start_node is None:
            return "[]"
        else:
            n = self.start_node
            message = "["
            while n is not None:
                message = message + "'" + str(n.item) + "'" + ", "
                n = n.ref
            message = message[:-2] + "]"
        return message
    
    def __len__(self):
        """ this method, is for len(), return the amount of elements in this list """
        return self._len
    
    def __iter__(self):
        """ this method if for the sentence 'for element in LinkedList: It allows the execute"""
        self.iter = self.start_node
        return self
    
    def __next__(self):
        """ this method if for the sentence 'for element in LinkedList: return one a one elements for each iteration """
        if self.iter == None:
            raise StopIteration()
        else:
            u = self.iter.item
            self.iter = self.iter.ref
            return u
            
    
if __name__=="__main__":
    # aqui pueden hacer sus pruebas para codear, pero no toquen el archivo test.py
    
    pass