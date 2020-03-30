import unittest

from my_foo import Foo

class TestMethod(unittest.TestCase):

	m = Foo()

	def test_case1(self):
		self.assertEqual(self.m.foo(1,1), 2, "Precisa ser 2")

	def test_case2(self):
		self.assertEqual(self.m.foo(-1,1), 1, "Precisa ser 1")

	def test_case3(self):
		self.assertEqual(self.m.foo(-1,-1), 1,  "Precisa ser 1")

	def suite():
		suite = unittest.TestSuite()
		suite.addTest(WidgetTestCase('test_case1'))
		suite.addTest(WidgetTestCase('test_case2'))
		suite.addTest(WidgetTestCase('test_case3'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


