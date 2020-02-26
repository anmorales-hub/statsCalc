import unittest
from RNG.randNum import RandNum
from RNG.randList import RandList
from RNG.listPick import ListPick


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [0, 1, 2, 3, 4]

    def test_randNum(self):
        result = RandNum.randNum(0, 10)
        self.assertEqual(int, type(result))

    def test_randNumSeed(self):
        result1 = RandNum.randNumSeed(4, 0, 10)
        result2 = RandNum.randNumSeed(4, 0, 10)
        self.assertEqual(True, result1 == result2)

    def test_randNumList(self):
        result1 = RandList.randList(4, 5, 0, 10)
        result2 = RandList.randList(4, 5, 0, 10)
        self.assertEqual(True, result1 == result2)

    def test_listPick(self):
        result = ListPick.listPick(self.test)
        x = None
        if result in self.test and type(result) == int:
            x = True
        self.assertEqual(True, x)

    def test_listPickSeed(self):
        result = ListPick.listPickSeed(3, self.test)
        result2 = ListPick.listPickSeed(3, self.test)
        x = None
        if result in self.test and type(result) == int:
            if result == result2:
                x = True
        self.assertEqual(True, x)

    def test_listPickList(self):
        temp = ListPick.listPickList(2, self.test)
        x = None
        if len(temp) == 2:
            for item in temp:
                if item in self.test and type(item) == int:
                    x = True
        self.assertEqual(True, x)

    def test_listPickListSeed(self):
        temp = ListPick.listPickListSeed(4, 2, self.test)
        temp2 = ListPick.listPickListSeed(4, 2, self.test)
        x = None
        if temp == temp2:
            x = True
        self.assertEqual(True, x)



if __name__ == '__main__':
    unittest.main()