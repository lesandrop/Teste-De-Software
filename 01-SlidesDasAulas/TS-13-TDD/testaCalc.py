import unittest

from Calc import Calculadora

class TestMethod(unittest.TestCase):

	calc=Calculadora()

	def test_caseSomaPositivo(self):
		soma = self.calc.soma(1,1)
		self.assertEqual(soma, 2, "Soma de 1 e 1 é 2")

	def test_caseSomaNegativo(self):
		soma = self.calc.soma(-1,-1)
		self.assertEqual(soma, -2, "Soma de -1 e -1 é -2")

	def test_caseSomaZero(self):
		soma = self.calc.soma(0,0)
		self.assertEqual(soma, 0, "Soma de 0 e 0 é 0")

	def test_caseSomaPositivoNegativo(self):
		soma = self.calc.soma(2,-1)
		self.assertEqual(soma, 1, "Soma de 2 e -1 é 1")