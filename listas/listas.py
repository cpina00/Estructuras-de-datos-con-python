class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None



class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def __str__(self):
        if self.start_node is None:
            print("List has no element")
        else:
            n = self.start_node
            message = "["
            while n is not None:
                message = message + "'" + str(n.item) + "'" + ", "
                n = n.ref
            message = message[:-2] + "]"
        return message

    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
        else:
            n = self.start_node
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    

                
    def __len__(self):
        n = self.start_node
        cont = 0
        while n is not None:
            cont += 1
            n = n.ref
        return cont
            
    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node
    
    
if __name__=="__main__":
    cont=2
    l = LinkedList() #    l.start_node = None
    l.insert_at_start("Juaquin Perez")
    l.insert_at_start("alejandra prieto")
    l.insert_at_start("emilio moyano")
    p = ["emilio moyano","alejandra prieto","Juaquin Perez"]
    #print("con ", cont, ": ",l)
    print(len(l))
    print(p)
    print(l)
