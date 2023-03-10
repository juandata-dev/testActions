#Archivo de ejemplo para las pruebas unitarias.
#El nombre del archivo debe iniciar con el prefijo test_

#Importar unittest para crear las pruebas unitarias
import unittest


#Clase de ejemplo, debe tener un nombre que termina con el sufijo TestCase, y conservar la herencia
class ExampleTestCase(unittest.TestCase):

	#Instancia el atributo logica para cada prueba
	def setUp(self):
		pass

    #Prueba para verificar que el caso funciona. El nombre del método usa el prefijo test_
	def test_nombre_claves_01(self):
		self.assertEqual(1, 1)

        
    def test_nombre_claves_02(self):
        self.assertEqual(1, 1)