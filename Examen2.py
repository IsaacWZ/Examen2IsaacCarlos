import unittest

class MiClase:
    def __init__(self, Valencia, Tempo, Tonos, listaCanciones, listaBailabilidad):
        self.Valencia = Valencia
        self.Tempo = Tempo
        self.Tonos = Tonos
        self.listaCanciones = listaCanciones
        self.listaBailabilidad = listaBailabilidad

    def ObtieneValencia(self, numero):
        # Convierte el número en una cadena para contar los dígitos impares
        numero_str = str(numero)
        digitos_impares = [int(digit) for digit in numero_str if int(digit) % 2 != 0]
        return len(digitos_impares)

    def DivisibleTempo(self, numero):
        divisores = [i for i in range(1, numero + 1) if numero % i == 0]
        return divisores

    def ObtieneMasBailable(self, lista):
        if not lista:
            return None
        return max(lista)

    def VerificaListaCanciones(self, lista):
        if any(song is None for song in lista):
            return False
        return True
################################################################################################
#Ejemplo de ejecución
# # Crear un objeto de la clase MiClase
# objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
# # Ejemplo de uso de los métodos
# print(objeto.ObtieneValencia(1234567))  # Debería imprimir 4
# print(objeto.DivisibleTempo(10))  # Debería imprimir [1, 2, 5, 10]
# print(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]))  # Debería imprimir 0.9
# print(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))  # Debería imprimir True
class TestMiClase(unittest.TestCase):
    def test_ObtieneValencia(self):
        mi_clase = MiClase(None, None, None, None, None)
        self.assertEqual(mi_clase.ObtieneValencia(12345), 3)
        self.assertEqual(mi_clase.ObtieneValencia(24680), 0)






    def test_DivisibleTempo(self):
        mi_clase = MiClase(None, None, None, None, None)

        self.assertEqual(mi_clase.DivisibleTempo(10), [1, 2, 5, 10])
        self.assertEqual(mi_clase.DivisibleTempo(7), [1, 7])




    def test_ObtieneMasBailable(self):
        mi_clase = MiClase(None, None, None, None, None)



    def test_VerificaListaCanciones(self):
        mi_clase = MiClase(None, None, None, None, None)
        self.assertTrue(mi_clase.VerificaListaCanciones([1, 2, 3, 4, 5]))
        self.assertFalse(mi_clase.VerificaListaCanciones([1, None, 3, 4, 5]))
if __name__ == '__main__':
    unittest.main()