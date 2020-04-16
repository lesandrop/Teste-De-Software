import unittest

from Foo import foo

class TestMethod(unittest.TestCase):

	def test_case1(self):
		self.assertEqual(foo(1,1), 2, "Precisa ser 2")

	def test_case2(self):
		self.assertEqual(foo(-1,1), 1, "Precisa ser 1")

	def test_case3(self):
		self.assertEqual(foo(-1,-1), 1,  "Precisa ser 1")

	def test_case4(self):
		self.assertEqual(foo(-1, 0), 0,  "Precisa ser 0")

if __name__ == '__main__':
    unittest.main()