import  unittest
from projects.pythonpro.calc import Calculate

class TestSum(unittest.TestCase):
    def test_sum(self):
        cal = Calculate()
        self.assertEqual(cal.add(1, 2), 3)
    def test_sub(self):
        cal = Calculate()
        self.assertEqual(cal.sub(7, 3), 4)

if __name__ == "__main__":
    unittest.main()