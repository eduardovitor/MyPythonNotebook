import unittest
from TwoSum import twoSum
class TestTwoSum(unittest.TestCase):
    def test_different_inputs(self):
        arr_test1 = [4,4,12,8]
        arr_test2 = [2,5,9]
        arr_test3 = [10,20,30,50,2,3,4,150,200,300,400]
        arr_test4 = [0,0,0,0,4,1,7,17]
        arr_test5 = [1,2]
        self.assertEqual(twoSum(arr_test1,20),[2,3])
        self.assertEqual(twoSum(arr_test2,14),[1,2])
        self.assertEqual(twoSum(arr_test3,23),[1,5])
        self.assertEqual(twoSum(arr_test4,5),[4,5])
        self.assertEqual(twoSum(arr_test5,3),[0,1])

if __name__ == "__main__":
    unittest.main()
