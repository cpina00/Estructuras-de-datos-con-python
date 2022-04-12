import unittest

from listas import LinkedList

class LinkedListTest(unittest.TestCase):
    
    """
    
    """
    def test_build_linkedList(self):
        l = LinkedList()
        p = []
        self.assertEqual(str(p),str(l))
    
    """
    
    """    
    def test_insert_at_start(self):
        l = LinkedList()
        l.insert_at_start("start_1")
        l.insert_at_start("start_2")
        l.insert_at_start("start_3")
        p = []
        p.insert(0,"start_1")
        p.insert(0,"start_2")
        p.insert(0,"start_3")
        self.assertEqual(str(p),str(l))

    """
    
    """
    def test_insert_at_end(self):
        l = LinkedList()
        l.insert_at_end("end_1")
        l.insert_at_end("end_2")
        l.insert_at_end("end_3")
        p = []
        p.append("end_1")
        p.append("end_2")
        p.append("end_3")
        self.assertEqual(str(l),str(p))
    
    """
    
    """    
    def test_len_1(self):
        l = LinkedList()
        l.insert_at_end("end_1")
        l.insert_at_start("start_1")
        self.assertEqual(2,len(l))
    
    """
    
    """    
    def test_len_2(self):
        l = LinkedList()
        self.assertFalse(len(l))
        
    """
    
    """
    def test_(self):
        pass

if __name__ == "__main__":
    unittest.main()

    