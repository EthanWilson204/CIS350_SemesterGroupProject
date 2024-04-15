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
        
        self.L1_speed = 3.0
        self.L2_speed = 1.5
        self.L3_speed = 0.75
        
        self.up1price, self.up2price, self.up3price = 300, 500, 700
        
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
    #test first bar
    def test_Upgrade_Bar_1(self):
        user_money = 10000
        bar_comps = [self.L1_speed, self.up1price, user_money]
        L1_speed, up1Price, new_user_money = Upgrade_Bar(bar_comps)
        
        self.assertLess(new_user_money, 10000)
        self.assertGreater(L1_speed, self.L1_speed)
        self.assertGreater(up1Price, self.up1price)
                
        self.assertEqual(L1_speed, self.L1_speed * 1.3)
        self.assertEqual(up1Price, self.up1price * 1.2)
        self.assertEqual(new_user_money, user_money - self.up1price)
    
    #test second bar
    def test_Upgrade_Bar_2(self):
        user_money = 10000
        bar_comps = [self.L2_speed, self.up2price, user_money]
        L2_speed, up2Price, new_user_money = Upgrade_Bar(bar_comps)
        
        self.assertLess(new_user_money, 10000)
        self.assertGreater(L2_speed, self.L2_speed)
        self.assertGreater(up2Price, self.up2price)
                
        self.assertEqual(L2_speed, self.L2_speed * 1.3)
        self.assertEqual(up2Price, self.up2price * 1.2)
        self.assertEqual(new_user_money, user_money - self.up2price)
    
    #test third bar
    def test_Upgrade_Bar_3(self):
        user_money = 10000
        bar_comps = [self.L3_speed, self.up3price, user_money]
        L3_speed, up3Price, new_user_money = Upgrade_Bar(bar_comps)
        
        self.assertLess(new_user_money, 10000)
        self.assertGreater(L3_speed, self.L3_speed)
        self.assertGreater(up3Price, self.up3price)
                
        self.assertEqual(L3_speed, self.L3_speed * 1.3)
        self.assertEqual(up3Price, self.up3price * 1.2)
        self.assertEqual(new_user_money, user_money - self.up3price)
        
        
    #test Start_Profit function
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
        
        
    #test Stop_Status function
    #test first status
    def test_Stop_Profit_1(self):
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        user_money = 500000
        status_active = False
        multiplier = 2
        
        #increase the speed of the bars, change status_active to True
        amt_comps = [L1A, L2A, L3A, user_money, status_active, self.status1Price]
        L1A, L2A, L3A, _, status_active, self.status1Price = Start_Profit(amt_comps, multiplier)
        
        #initialize the stop components with the increased bar speeds and true status.
        #return components to original values
        stop_comps = [L1A, L2A, L3A, status_active]
        L1A, L2A, L3A, status_active = Stop_Profit(stop_comps, multiplier)
        
        self.assertEqual(L1A, self.L1_Amt)
        self.assertEqual(L2A, self.L2_Amt)
        self.assertEqual(L3A, self.L3_Amt)
        self.assertEqual(status_active, False)
  
    #test second status (different multiplier)
    def test_Stop_Profit_2(self):
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        user_money = 500000
        status_active = False
        multiplier = 5
        
        #increase the speed of the bars, change status_active to True
        amt_comps = [L1A, L2A, L3A, user_money, status_active, self.status2Price]
        L1A, L2A, L3A, _, status_active, self.status2Price = Start_Profit(amt_comps, multiplier)
        
        #initialize the stop components with the increased bar speeds and true status.
        #return components to original values
        stop_comps = [L1A, L2A, L3A, status_active]
        L1A, L2A, L3A, status_active = Stop_Profit(stop_comps, multiplier)
        
        self.assertEqual(L1A, self.L1_Amt)
        self.assertEqual(L2A, self.L2_Amt)
        self.assertEqual(L3A, self.L3_Amt)
        self.assertEqual(status_active, False)
    
    #test third status (different multiplier)
    def test_Stop_Profit_3(self):
        L1A, L2A, L3A = self.L1_Amt, self.L2_Amt, self.L3_Amt
        user_money = 500000
        status_active = False
        multiplier = 7.5
        
        #increase the speed of the bars, change status_active to True
        amt_comps = [L1A, L2A, L3A, user_money, status_active, self.status3Price]
        L1A, L2A, L3A, _, status_active, self.status3Price = Start_Profit(amt_comps, multiplier)
        
        #initialize the stop components with the increased bar speeds and true status.
        #return components to original values
        stop_comps = [L1A, L2A, L3A, status_active]
        L1A, L2A, L3A, status_active = Stop_Profit(stop_comps, multiplier)
        
        self.assertEqual(L1A, self.L1_Amt)
        self.assertEqual(L2A, self.L2_Amt)
        self.assertEqual(L3A, self.L3_Amt)
        self.assertEqual(status_active, False)