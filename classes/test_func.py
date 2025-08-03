import unittest

def sum(a, b):
    return a + b

class sumtest(unittest.TestCase):
        # arrange
        def setUp(self):
            self.a = 10
            self.b = 20
            print("setUp called...")

        def tearDown(self):
             a = 0
             b = 0
             print("tearDown called...")

        def test_func_1(self):
            print("Test 1- called...")
            # act
            result = self.a + self.b
            # assert
            self.assertEqual(result, self.a + self.b)


        def test_func_2(self):
            print("test 2- called...")
            # act
            result = self.a + self.b
            # assert
            self.assertEqual(result, self.a + self.b)


if __name__ == "__main__":
     unittest.main()
