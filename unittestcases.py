import unittest
from pylint import lint
from codefile import methods

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(methods.add(3,4,5), 12)
        self.assertEqual(methods.add(4,5), 9)
        self.assertEqual(methods.add(-3,4,-1), 0)
        self.assertEqual(methods.add(1000,0,-10), 990)
        
    def test_subtract(self):
        self.assertEqual(methods.subtract(3,4,5), -6)
        self.assertEqual(methods.subtract(-4,5), -9)
        self.assertEqual(methods.subtract(-3,4,-1), -6)
        
    def test_multiply(self):
        self.assertEqual(methods.multiply(3,4,5), 60)
        self.assertEqual(methods.multiply(4,5), 20)
        self.assertEqual(methods.multiply(-3,4,-1), 12)
#         self.assertEqual(methods.multiply(1000,0,-10), 0)
        self.assertEqual(methods.multiply(1000,0,-10), 10)
       
    def test_pylint(self):
        results = lint.Run(['codefile/methods.py'],do_exit=False)
        score = results.linter.stats['global_note']
        print('pylint score : '+str(score))
        self.assertTrue(score >6)
        
if __name__ =='__main__':
    unittest.main()
