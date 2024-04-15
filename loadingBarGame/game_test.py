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
        self.status1Price = 50000
        self.status2Price = 100000
        self.status3Price = 1000
        
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
        
        
        
        
        
        
    #test Upgrade_Bar
    #test profit multipliers 
    def test_Start_Profit_1(self):
        
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        statusPrice = self.status1Price
        user_money = 500000
        status_active = False
        multiplier = 2
        
        amt_comps = [L1A, L2A, L3A, user_money, status_active, statusPrice]
        L1A, L2A, L3A, _, _, _ = Start_Profit(amt_comps, multiplier)
        #L1A, L2A, L3A, user_money, status_active, statusPrice = Upgrade_Bar(amt_comps, multiplier)
        
        self.assertGreater(L1A, self.L1_Amt)
        self.assertGreater(L2A, self.L2_Amt)
        self.assertGreater(L3A, self.L3_Amt)
        
        self.assertEqual(L1A, self.L1_Amt * multiplier)
        self.assertEqual(L2A, self.L2_Amt * multiplier)
        self.assertEqual(L3A, self.L3_Amt * multiplier)
    
    #test first status button
    def test_Start_Profit_2(self):
        
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        statusPrice = self.status1Price
        user_money = 500000
        status_active = False
        multiplier = 2
        
        amt_comps = [L1A, L2A, L3A, user_money, status_active, statusPrice]
        _, _, _, user_money, status_active, statusPrice = Start_Profit(amt_comps, multiplier)
        
        self.assertLess(user_money, 500000)
        self.assertNotEqual(status_active, False)
        
        self.assertEqual(user_money, 500000 - self.status1Price)
        self.assertEqual(status_active, True) 
    
    #test second status button
    def test_Start_Profit_3(self):
        
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        statusPrice = self.status2Price
        user_money = 500000
        status_active = False
        multiplier = 2
        
        amt_comps = [L1A, L2A, L3A, user_money, status_active, statusPrice]
        _, _, _, user_money, status_active, statusPrice = Start_Profit(amt_comps, multiplier)
        
        self.assertLess(user_money, 500000)
        self.assertNotEqual(status_active, False)
        
        self.assertEqual(user_money, 500000 - self.status2Price)
        self.assertEqual(status_active, True) 
    
    #test third status button
    def test_Start_Profit_4(self):
        
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        statusPrice = self.status3Price
        user_money = 500000
        status_active = False
        multiplier = 2
        
        amt_comps = [L1A, L2A, L3A, user_money, status_active, statusPrice]
        _, _, _, user_money, status_active, statusPrice = Start_Profit(amt_comps, multiplier)
        
        self.assertLess(user_money, 500000)
        self.assertNotEqual(status_active, False)
        
        self.assertEqual(user_money, 500000 - self.status3Price)
        self.assertEqual(status_active, True)