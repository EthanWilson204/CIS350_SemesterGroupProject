'''
Project: Money Loader
Class: CIS 350-02
Professor: J. Nandigham
Authors: Ethan Wilson, Gideon Moerdyk, Gabe Kucinich

Description:
A game where you load bars to earn money towards a total. Everytime a bar loads, money is added to the total.
You can spend money to upgrade the speed of each bar to earn money faster. Once the total is reached, the game
is complete and a time will be displayed showing how fast it was completed. Figure out how to beat the game as
fast as possible.
'''
#imports
import pygame
from sys import exit
from Screen import *
from GameFunctions import *

#initialize pygame
pygame.init()
CLOCK = pygame.time.Clock()

#initialize some fonts
L1ValueDisplay = pygame.font.SysFont('Ariel',40)
L2ValueDisplay = L1ValueDisplay
L3ValueDisplay = L1ValueDisplay
moneyDisplay = pygame.font.SysFont('Ariel',100)
status1PriceDisplay = pygame.font.SysFont('Ariel',30)
upgradeFont = pygame.font.SysFont('Ariel',50,bold=False)
purchaseFont  = pygame.font.SysFont('Ariel',45,bold=False)

#-------------------------------------------------------------------------------------------------------------------------------

def displayTimer():
    surfFT = fontFT.render("Time: " + str(game_time), True, 'white')
    screen.blit(surfFT, (800,70))
    
def displayL1Value(L1Value):
    L1Value = L1ValueDisplay.render("$" + str(L1Value), True, (0,0,0))
    screen.blit(L1Value, (660,360))
        
def displayL2Value(L2Value):
    L2Value = L2ValueDisplay.render("$" + str(L2Value), True, (0,0,0))
    screen.blit(L2Value, (660,510))
         
def displayL3Value(L3Value):
    L3Value = L3ValueDisplay.render("$" + str(L3Value), True, (0,0,0))
    screen.blit(L3Value, (660,660))
         
def displayMoney (money):
    moneyComma = (f"{money:,}")
    moneyComma = moneyDisplay.render("$" + moneyComma, True, (255,255,255))
    screen.blit(moneyComma, (300,70))

def displaystatus1Price(status1Price):
    status1Price = status1PriceDisplay.render("$" + str(status1Price), True, (255,255,255))
    screen.blit(status1Price, (100,305))
         
# Display Upgrade Bar 1 Price
def displayup1Price (up1Price):
    up1Price = up1PriceDisplay.render("$" + str(up1Price), True, (0,0,0))
    screen.blit(up1Price, (1100,355))

# Display Upgrade Bar 2 Price
def displayup2Price (up2Price):
    up2Price = up2PriceDisplay.render("$" + str(up2Price), True, (0,0,0))
    screen.blit(up2Price, (1100,505))

# Display Upgrade Bar 3 Price
def displayup3Price (up3Price):
    up3Price = up3PriceDisplay.render("$" + str(up3Price), True, (0,0,0))
    screen.blit(up3Price, (1100,655))   

#-------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    #main display
    screen_width = 1300
    screen_height = 750
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill('Dark Grey')
    pygame.display.set_caption("Main Game")

    #define start and end for bars
    start_x = 320
    load_limit = 1000

    #define tax value
    taxVal = 999

    #define bar positions
    L1_xpos = start_x
    L1_ypos = 300
    L2_xpos = start_x
    L2_ypos = 450
    L3_xpos = start_x
    L3_ypos = 600
    bar_length = 50
    bar_height = 50


    #define bar speeds
    L1_speed = 0 #going to 3.0
    L2_speed = 0 #going to 1.5
    L3_speed = 0 #going to 0.75

    #Draw buttons
    #bar height and length are 50
    B1_surf = pygame.Surface((0,0))
    B2_surf = pygame.Surface((0,0))
    B3_surf = pygame.Surface((0,0))

    B1_surf.fill('black')
    B2_surf.fill('black')
    B3_surf.fill('black')
    
    #get rectangles to make button functional
    B1_rect = B1_surf.get_rect()
    B2_rect = B2_surf.get_rect()
    B3_rect = B3_surf.get_rect()
    
    SetBackground(screen, screen_width, screen_height, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos)

# Loading Bars
    # Bar 1
    L1_Bar = pygame.Surface((bar_length,bar_height))
    L1_Bar.fill('red')
    L1Value = 100

    # Bar 2
    L2_Bar = L1_Bar.copy()
    L2_Bar.fill('green')
    L2Value = 200
  
    # Bar 3
    L3_Bar = L1_Bar.copy()
    L3_Bar.fill('blue')
    L3Value = 300

    
#-------------------------------------------------------------------------------------------------------------------------------
# Money System
    # Define money variables
    money_goal = 1000000 #$1,000,000
    user_money = 500000
    L1_Amt = 100
    L2_Amt = 200
    L3_Amt = 300

#-------------------------------------------------------------------------------------------------------------------------------
# Buttons
    # Quit button
    font0 = pygame.font.SysFont('Ariel',70)
    surf0 = font0.render('Quit', True, 'black')
    exitButton = pygame.Rect(1180,10,110,60)

    # Button Rectangles
    up1Button = pygame.Rect(1100,300,150,50)
    up2Button = pygame.Rect(1100,450,150,50)
    up3Button = pygame.Rect(1100,600,150,50)

    # Initial Prices of Buttons
    up1Price = 0 #then go to 300
    up2Price = 1000
    up3Price = 2000

    # Upgrade Bar 1 button
    upgradeSurf1 = upgradeFont.render('Upgrade', True, 'white')
    purchaseSurf1 = purchaseFont.render('Purchase', True, 'white')

    # Upgrade Bar 2 button
    upgradeSurf2 = upgradeFont.render('Upgrade', True, 'white')
    purchaseSurf2 = purchaseFont.render('Purchase', True, 'white')

    # Upgrade Bar 3 button
    upgradeSurf3 = upgradeFont.render('Upgrade', True, 'white')
    purchaseSurf3 = purchaseFont.render('Purchase', True, 'white')

    # Fonts for price display
    up1PriceDisplay = pygame.font.SysFont('Ariel',40)
    up2PriceDisplay = pygame.font.SysFont('Ariel',40)
    up3PriceDisplay = pygame.font.SysFont('Ariel',40)

    # Status Buttons
    statusFont = pygame.font.SysFont('Ariel',50,bold=False)
    statusSurf = statusFont.render('Profit x2', True, 'white')
    cooldownStatusSurf = statusFont.render(' Active!', True, 'white')

    status1Button = pygame.Rect(50,250,150,50)

    status1Price = 300 #just for testing, price will change
    statusActive = False
    time_limit = 0

    
    
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- GAME RUN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    #set up timer
    game_time = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    fontFT = pygame.font.SysFont('Ariel', 100, bold=False)
    
    #Run the events in game
    gamerun = True
    ticknum = 60 #60 fps

    #Within the game loop
    while gamerun:
    # Display Money and Timer
        blitScoreboard(screen, screen_width, screen_height)
        user_money = round(user_money, 0)
        displayMoney(user_money)
        displayTimer()

    # Display price of each status effect
        displaystatus1Price(status1Price)

    #TAXES, apply a 50% tax on money so long as the player has not won the game and has money to tax
        if user_money < money_goal and user_money > 0.0:
            #set the user_money equal to the returned taxed value based on RNG
            user_money = taxes(user_money, taxVal)#have a taxVal chance for taxes each tick

     # Check if player meets goal
        if user_money >= money_goal:
            
            # Stop bars from loading and stop earning more money once game is won
            L1_speed = 0 
            L2_speed = 0 
            L3_speed = 0
            user_money = 1000000

        for event in pygame.event.get():

            # Check if player quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            #update the time by one second
            if event.type == pygame.USEREVENT:
                #check if game is started
                if L1_speed == 0 and user_money < 1000000:
                    game_time = 0
                elif L1_speed == 0 and user_money >= 1000000:
                    displayTimer()
                else:
                    game_time += 1

            # Display value of each loading bar
            displayL1Value(L1Value)
            displayL2Value(L2Value)
            displayL3Value(L3Value)


            # Round Up Prices
            up1Price = round(up1Price, 0)
            up2Price = round(up2Price, 0)
            up3Price = round(up3Price, 0)

            # Display Upgrade Bar Prices
            blitUpPrices(screen)
            displayup1Price(up1Price)
            displayup2Price(up2Price)
            displayup3Price(up3Price)
            
            # Exit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if exitButton.collidepoint(event.pos):
                        pygame.quit()
                        exit()

            # Upgrade Bar 1 button
            if user_money >= up1Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up1Button.collidepoint(event.pos):
                            
                            if L1_speed == 0:
                                 L1_speed = 3.0
                                 up1Price = 300
                            else:
                                L1_speed *= 1.3
                                user_money -= up1Price
                                up1Price *= 1.2

            # Upgrade Bar 2 button
            if user_money >= up2Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up2Button.collidepoint(event.pos):
                            if L2_speed == 0:
                                 L2_speed = 1.5
                                 up2Price = 500
                                 user_money -= 1000
                            else:
                                L2_speed *= 1.3
                                user_money -= up2Price
                                up2Price *= 1.2

            # Upgrade Bar 3 button
            if user_money >= up3Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up3Button.collidepoint(event.pos):
                            if L3_speed == 0:
                                 L3_speed = 0.75
                                 up3Price = 700
                                 user_money -= 2000
                            else:
                                L3_speed *= 1.3
                                user_money -= up3Price
                                up3Price *= 1.2

            # Status 1 button
            if statusActive == False:
                if user_money >= status1Price:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if status1Button.collidepoint(event.pos):
                                user_money -= status1Price
                                statusActive = True
                                time_limit = int(game_time) + 10
                                L1_Amt *= 2
                                L2_Amt *= 2
                                L3_Amt *= 2

            if statusActive == True:
                if int(game_time) >= time_limit:
                    L1_Amt /= 2
                    L2_Amt /= 2
                    L3_Amt /= 2
                    statusActive = False



#-------------------------------------------------------------------------------------------------------------------------------
        # Exit button
        
        a,b = pygame.mouse.get_pos()
        if exitButton.x <= a <= exitButton.x + 110 and exitButton.y <= b <= exitButton.y + 60:
            pygame.draw.rect(screen,(255,25,25),exitButton)
        else:
            pygame.draw.rect(screen,(200,0,0),exitButton)
        screen.blit(surf0,(exitButton.x+5, exitButton.y+5))  
#-------------------------------------------------------------------------------------------------------------------------------
        # Upgrade Bar 1 button
    
        if up1Button.x <= a <= up1Button.x + 150 and up1Button.y <= b <= up1Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up1Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up1Button)
        if L1_speed == 0:
            screen.blit(purchaseSurf1,(up1Button.x+5, up1Button.y+5))
        else:
            screen.blit(upgradeSurf1,(up1Button.x+5, up1Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------        
        # Upgrade Bar 2 button
        
        if up2Button.x <= a <= up2Button.x + 150 and up2Button.y <= b <= up2Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up2Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up2Button)
        if L2_speed == 0:
            screen.blit(purchaseSurf2,(up2Button.x+5, up2Button.y+5))
        else:
            screen.blit(upgradeSurf2,(up2Button.x+5, up2Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------        
        # Upgrade Bar 3 button
        
        if up3Button.x <= a <= up3Button.x + 150 and up3Button.y <= b <= up3Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up3Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up3Button)
        if L3_speed == 0:
            screen.blit(purchaseSurf3,(up3Button.x+5, up3Button.y+5))
        else:
            screen.blit(upgradeSurf3,(up3Button.x+5, up3Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------
       # Status 1 button
        
        if statusActive == False:
            if status1Button.x <= a <= status1Button.x + 150 and status1Button.y <= b <= status1Button.y + 50:
                pygame.draw.rect(screen,(150,0,0),status1Button)
            else:
                pygame.draw.rect(screen,(200,0,0),status1Button)
            screen.blit(statusSurf,(status1Button.x+5, status1Button.y+5))
        else:
            pygame.draw.rect(screen,(0,200,0),status1Button)
            screen.blit(cooldownStatusSurf,(status1Button.x+5, status1Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------
        #Loading Bar Animations

        # Loading bar 1
        L1_xpos += L1_speed
        L2_xpos += L2_speed
        L3_xpos += L3_speed
                
        if L1_xpos > load_limit:
            
            user_money += L1_Amt
            L1_xpos = start_x
            pygame.draw.rect(screen, 'white', (L1_xpos, L1_ypos, 740, bar_height))
        
        # Loading bar 2
        if L2_xpos > load_limit:
            
            user_money += L2_Amt
            L2_xpos = start_x
            pygame.draw.rect(screen, 'white', (L2_xpos, L2_ypos, 740, bar_height))

        # Loading bar 3
        if L3_xpos > load_limit:
            
            user_money += L3_Amt
            L3_xpos = start_x
            pygame.draw.rect(screen, 'white', (L3_xpos, L3_ypos, 740, bar_height))
            
        screen.blit(L1_Bar,(L1_xpos,L1_ypos))
        screen.blit(L2_Bar,(L2_xpos,L2_ypos))
        screen.blit(L3_Bar,(L3_xpos,L3_ypos))
            
#-------------------------------------------------------------------------------------------------------------------------------
        
        pygame.display.update()
        CLOCK.tick(ticknum)#cap framerate at 60 fps     

    pygame.quit()
    exit()
