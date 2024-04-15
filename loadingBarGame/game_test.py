import unittest
from Game import *
from GameFunctions import *
from Screen import *
from pygame import display

class TestGame(unittest.TestCase):
    
    #unchanging values from game
    #included here to avoid scope issues
    def setUp(self):
        display.init()
        self.load_limit = 1000
        self.start_x = 320
        self.L1_Amt = 100
        self.L2_Amt = 200
        self.L3_Amt = 300
        
    def tearDown(self):
        display.quit()

    #test Add_Reset
    #when user money is 0
    def test_Add_Reset_1(self):
        
        user_money, L1_xpos = Add_Reset(self.L1_Amt, self.load_limit, self.start_x, 0)
        self.assertEqual(user_money, 100)
        self.assertEqual(L1_xpos, self.start_x)
    
    #when user money is not 0
    def test_Add_Reset_2(self):
        
        user_money, L1_xpos = Add_Reset(self.L1_Amt, self.load_limit, self.start_x, 10000)
        self.assertEqual(user_money, 10100)
        self.assertEqual(L1_xpos, self.start_x)
    
    
    #when user money is 0
    def test_Add_Reset_3(self):
        
        user_money, L2_xpos = Add_Reset(self.L2_Amt, self.load_limit, self.start_x, 0)
        self.assertEqual(user_money, 200)
        self.assertEqual(L2_xpos, self.start_x)
        
    #when user money is not 0
    def test_Add_Reset_4(self):
        
        user_money, L2_xpos = Add_Reset(self.L2_Amt, self.load_limit, self.start_x, 10000)
        self.assertEqual(user_money, 10200)
        self.assertEqual(L2_xpos, self.start_x)
    
    #when user money is 0
    def test_Add_Reset_5(self):
        
        user_money, L3_xpos = Add_Reset(self.L3_Amt, self.load_limit, self.start_x, 0)
        self.assertEqual(user_money, 300)
        self.assertEqual(L3_xpos, self.start_x)
    
    #when user money is not 0
    def test_Add_Reset_6(self):
        
        user_money, L3_xpos = Add_Reset(self.L3_Amt, self.load_limit, self.start_x, 10000)
        self.assertEqual(user_money, 10300)
        self.assertEqual(L3_xpos, self.start_x)
        
    
    
    
    
    
    
    
        

    """
    def test_Upgrade_Bar(self):
        
        
    def test_Start_Profit(self):
        
        
    def test_Stop_Profit(self):
    """
