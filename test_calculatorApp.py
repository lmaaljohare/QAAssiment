from ast import Add
from asyncio.windows_events import NULL
from decimal import DivisionUndefined
import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup")

    def test_AddTestCase(self):
        res = add(3,1)
        self.assertEqual(res, 4)


    def test_multipyTestCase(self):
        res = multiply(2,2)
        self.assertEqual(multiply(2,2), 4)


    def test_DivideTest1(self):
        self.assertRaises(ZeroDivisionError, divide,1,0)    
    def test_DivideTest2(self):
        res = divide(0,2)
        self.assertEqual(res, 0)
    def test_DivideTest3(self):
        res = divide(8,4)
        self.assertEqual(res, 2)

    def test_isExitTest1(self):
        res = isExit("no")
        self.assertEqual(res, True)
    def test_isExitTest2(self):
        res = isExit("yes")
        self.assertEqual(res, False)  
    def test_isExitTest3(self):
        self.assertRaises(ValueError, isExit, "Yes") 

        
    def test_subtractTestCase(self):
        res = subtract(4,1)
        self.assertEqual(res, 3)  
        
        
    def test_checkUserInputTest1(self):
        self.assertEqual(check_user_input(1), 1)
    def test_checkUserInputTest2(self):
        self.assertEqual(check_user_input("2.1"),2.1) ###################
    def test_checkUserInputTest3(self):
        self.assertRaises(ValueError, check_user_input, "")    
    def test_checkUserInputTest4(self):
        self.assertRaises(ValueError, check_user_input, "y")    
        

    def test_checkCalculateTest1(self):
        self.assertRaises(Exception, calculate, "6",2,2)  
    def test_checkCalculateTest2(self):
        self.assertRaises(ZeroDivisionError, calculate ,"4",1,"0")
    def test_checkCalculateTest3(self):
        with mock.patch('calculatorApp.add', return_value = 7):
            res = calculate('1',4,3)
        self.assertEqual(res, 7)    
    def test_checkCalculateTest4(self):
        with mock.patch('calculatorApp.subtract', return_value = 3):
            res = calculate('2',6,3)
        self.assertEqual(res, 3)      
    def test_checkCalculateTest5(self):
        with mock.patch('calculatorApp.multiply', return_value = 8):
            res = calculate('3',2,4)
        self.assertEqual(res, (2,'*',4,'=',8))      
    def test_checkCalculateTest6(self):
        with mock.patch('calculatorApp.divide', return_value = 4):
            res = calculate('4',8,2)
        self.assertEqual(res, (8,'/',2,'=',4))           
    def test_checkCalculateTest7(self):
        self.assertRaises(ValueError,calculate ,"4", "", "")
        


if __name__ == '__main__':
	unittest.main()
