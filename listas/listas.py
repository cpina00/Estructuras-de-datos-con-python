class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None
        self._len = 0
        self.iter = self.start_node
    
    def __str__(self):
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

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
        self.iter = self.start_node
        self._len +=1
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            self.iter = self.start_node
        else:
            n = self.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
        self._len +=1
    
    def insert_to_index(self,index,data):
        pass
    
    def remove_to_begin(self):
        pass
    
    def remove_to_end(self):
        pass
    
    def remove_to_index(self,index):
        pass
    
      
    def __len__(self):
        return self._len
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iter == None:
            raise StopIteration()
        else:
            u = self.iter.item
            self.iter = self.iter.ref
            return u
            
    
if __name__=="__main__":
    cont=2
    l = LinkedList() #    l.start_node = None
    l.insert_at_start("Juaquin Perez")
    l.insert_at_start("alejandra prieto")
    l.insert_at_start("emilio moyano")
    p = ["emilio moyano","alejandra prieto","Juaquin Perez"]
    a = []
    b = LinkedList()
    #print("a:",a,"b:",b)
    #print("con ", cont, ": ",l)
    #print(len(l))
    #print(p)
    #print(l)
