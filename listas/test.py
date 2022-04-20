# -------------------------------------------------------------------
#                   NO MODIFICAR ESTE ARCHIVO
# -------------------------------------------------------------------



import unittest

from listas import LinkedList

# Los comentarios con tres comillas dobles, son 'doc string', lo que significa que python, los considerará
# como parte de la docmuentación de las clases o métodos correspondientes. 
# En cado de errores, se mostrará por pantalla esos mensajes, para encontrar rápidamente donde está el error

class LinkedListTest(unittest.TestCase):
    """
    Clase para medir los resultados de distintos métodos de la clase LinkedList, comparado con la clase list, 
    nativa de python, para manejar listas. Ambas clases deben retornar lo mismo para aprobar los test.
    """
    
    def test_build_linkedList(self):
        """
        Este test compara el constructor de la clase LinkedList con la clase nativa de python. 
        Si son iguales, pasa el test. 
        """
        l = LinkedList()
        p = []
        self.assertEqual(str(p),str(l))
    
    def test_insert_at_start(self):
        """
        Este test pone a prueba el método insert_at_start de la clase LinkedList, comparando con la clase nativa,
        si los resultados son iguales, pasa el test.
        """ 
        l = LinkedList()
        l.insert_at_start("start_1")
        l.insert_at_start("start_2")
        l.insert_at_start("start_3")
        p = []
        p.insert(0,"start_1")
        p.insert(0,"start_2")
        p.insert(0,"start_3")
        self.assertEqual(str(p),str(l))

    def test_insert_at_end(self):
        """
        Este test pone a prueba el método insert_at_end de la clase LinkedList, comparando con la clase nativa,
        si los resultados son iguales, pasa el test.
        """
        l = LinkedList()
        l.insert_at_end("end_1")
        l.insert_at_end("end_2")
        l.insert_at_end("end_3")
        p = []
        p.append("end_1")
        p.append("end_2")
        p.append("end_3")
        self.assertEqual(str(l),str(p))
        
    def test_len_1(self):
        """
        Este test determina el 'largo' de la lista LinkedList, y su resultado cuando se aplica la función len() a sus objetos
        """
        l = LinkedList()
        l.insert_at_end("end_1")
        l.insert_at_start("start_1")
        self.assertEqual(2,len(l))
      
    def test_len_2(self):
        """
        Este test determina el 'largo' de la lista LinkedList, y su resultado cuando se aplica la función len() a sus objetos
        mide particularmente, que el constructor entregue bien su valor.
        """
        l = LinkedList()
        self.assertFalse(len(l))
          
    # -------------------------------------------------------------------
    # Los test anteriores, ya están probados y todos funcionan. si alguno
    # de ellos falla, es por que 'se rompió' el código, y deben buscar 
    # el error en las modificaciones que han ido realizando.
    # -------------------------------------------------------------------


    # -------------------------------------------------------------------
    # Los test a continuación, medirán los métodos que ustedes creen.
    # evalúa el buen comportamiento de ellos, comparado con los métodos
    # de la clase list netiva de python 
    # -------------------------------------------------------------------

    def test_insert_to_index_1(self):
        """
        prueba para el método insert_to_index, que debe agregar un elemento en el 
        index entregado. hace lo mismo que el método insert(i) de las listas nativas. 
        insert_to_index(0,data) es igual a insert_at_start(data) 
        """
        l = LinkedList()
        l.insert_to_index(0,"index_1")
        l.insert_to_index(0,"index_2")
        l.insert_to_index(0,"index_3")
        p = LinkedList()
        p.insert_at_start("index_1")
        p.insert_at_start("index_2")
        p.insert_at_start("index_3")
        self.assertEqual(str(l),str(p))
        
    def test_insert_to_index_2(self):
        """
        prueba para el método insert_to_index, que debe agregar un elemento en el 
        index entregado. hace lo mismo que el método insert(i) de las listas nativas. 
        insert_to_index(len(LinkedList),data) es igual a insert_at_end(data)
        """
        l = LinkedList()
        l.insert_to_index(len(l),"index_1")
        l.insert_to_index(len(l),"index_2")
        l.insert_to_index(len(l),"index_3")
        p = LinkedList()
        p.insert_at_end("index_1")
        p.insert_at_end("index_2")
        p.insert_at_end("index_3")
        self.assertEqual(str(l),str(p))
        
    def test_insert_to_index_3(self):
        """
        prueba para el método insert_to_index, que debe agregar un elemento en el 
        index entregado. hace lo mismo que el método insert(i, data) de las listas nativas. 
        """
        l = LinkedList()
        l.insert_at_start("test_1")
        l.insert_at_start("test_2")
        l.insert_at_start("test_3")
        l.insert_at_start("test_4")
        l.insert_to_index(2,"test_index")
        p = []
        p.insert(0,"test_1")
        p.insert(0,"test_2")
        p.insert(0,"test_3")
        p.insert(0,"test_4")
        p.insert(2,"test_index")
        self.assertEqual(str(l),str(p))
    
    def test_remove_to_begin(self):
        """
        prueba para el método remove_to_begin que elimina el primer elemento de la lista.
        es igual a la función pop(0) de la clase nativa de python
        """
        l = LinkedList()
        l.insert_at_start("start_1")
        l.insert_at_start("start_2")
        l.insert_at_start("start_3")
        l.remove_to_begin()
        
        p = []
        p.insert(0,"start_1")
        p.insert(0,"start_2")
        p.insert(0,"start_3")
        p.pop(0)
        self.assertEqual(str(l),str(p))
    
    def test_remove_to_end(self):
        """
        prueba para el método remove_to_end que elimina el primer elemento de la lista.
        es igual a la función pop() de la clase nativa de python
        """
        l = LinkedList()
        l.insert_at_start("start_1")
        l.insert_at_start("start_2")
        l.insert_at_start("start_3")
        l.remove_to_end()
        
        p = []
        p.insert(0,"start_1")
        p.insert(0,"start_2")
        p.insert(0,"start_3")
        p.pop()
        self.assertEqual(str(l),str(p))
        
    def test_remove_to_index(self):
        """
        prueba para el método remove_to_begin que elimina el primer elemento de la lista.
        es igual a la función pop(i) de la clase nativa de python
        """
        l = LinkedList()
        l.insert_at_start("test_1")
        l.insert_at_start("test_2")
        l.insert_at_start("test_3")
        l.insert_at_start("test_4")
        l.remove_to_index(2)
        p = []
        p.insert(0,"test_1")
        p.insert(0,"test_2")
        p.insert(0,"test_3")
        p.insert(0,"test_4")
        p.pop(2)
        self.assertEqual(str(l),str(p))
        
    def test_len_3(self):
        """
        Este test determina el 'largo' de la lista LinkedList, y su resultado cuando se aplica la función len() a sus objetos
        """
        l = LinkedList()
        l.insert_at_end("end_1")
        l.insert_at_start("start_1")
        l.insert_to_index(1,"algo")
        l.insert_to_index(1,"algo")
        l.remove_to_begin()
        l.remove_to_end()
        self.assertEqual(2,len(l))
        
    
        

if __name__ == "__main__":
    unittest.main()

    