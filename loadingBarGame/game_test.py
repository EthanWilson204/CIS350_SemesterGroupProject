import unittest
from Game import *
from GameFunctions import *
from pygame import display

class GameTest(unittest.TestCase):
    
    def setUp(self):
        display.init()
        
    def tearDown(self):
        display.quit()
    #dont write tests for UI, write tests for things not with the UI
    #test to see if money is rendered properly for car 1, 2, and 3
    def test_displayL1Value_1(self):
        L1Value = displayL1Value.render("$" + str(100), True, (0,0,0))
        self.assertEqual(L1Value, "$100")
        
    #test to see if the initial upgrade costs are correct
    
    #test to see if an instance of pressing the button once renders properly
    
    #test to see if an instance of pressing the button after once calculates the upgrade cost correctly
    
    #test to see if the positions of the bars change by x amount after certain number of blits
    
    #test to see if the bar position resets to start_x after reaching end of bar
    
    #test to see if user money for bar 1, 2 and 3 adds correct money to the total