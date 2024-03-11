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
    
    SetBackground(screen, screen_width, screen_height, B1_surf, B2_surf, B3_surf, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos)

#-------------------------------------------------------------------------------------------------------------------------------
        
    def displayTimer():
         timerDisplay = pygame.font.SysFont('Ariel',60)
         timer = pygame.time.get_ticks()
         timer /= 1000
         timer = round(timer)


         displayTimer = timerDisplay.render(str(timer), True, (255,255,255))
         screen.blit(displayTimer, (1180,75))#blit stands for block image transfer... i.e. put one surface on another

#-------------------------------------------------------------------------------------------------------------------------------
# Loading Bars
    # Bar 1
    L1_Bar = pygame.Surface((bar_length,bar_height))
    L1_Bar.fill('red')

    L1Value = 100
    L1ValueDisplay = pygame.font.SysFont('Ariel',40)
    def displayL1Value(L1Value):
         L1Value = L1ValueDisplay.render("$" + str(L1Value), True, (0,0,0))
         screen.blit(L1Value, (660,360))

    # Bar 2
    L2_Bar = L1_Bar.copy()
    L2_Bar.fill('green')

    L2Value = 200
    L2ValueDisplay = pygame.font.SysFont('Ariel',40)
    def displayL2Value(L2Value):
         L2Value = L2ValueDisplay.render("$" + str(L2Value), True, (0,0,0))
         screen.blit(L2Value, (660,510))


    # Bar 3
    L3_Bar = L1_Bar.copy()
    L3_Bar.fill('blue')

    L3Value = 300
    L3ValueDisplay = pygame.font.SysFont('Ariel',40)
    def displayL3Value(L3Value):
         L3Value = L3ValueDisplay.render("$" + str(L3Value), True, (0,0,0))
         screen.blit(L3Value, (660,660))
#-------------------------------------------------------------------------------------------------------------------------------
# Money System
    # Define money variables
    money_goal = 1000000 #$1,000,000
    user_money = 999750 #TODO set back to 0 for the game release
    L1_Amt = 100
    L2_Amt = 200
    L3_Amt = 300

    moneyDisplay = pygame.font.SysFont('Ariel',100)

    def displayMoney (money):
         money = moneyDisplay.render("$" + str(money), True, (255,255,255))
         screen.blit(money, (300,70))

#-------------------------------------------------------------------------------------------------------------------------------
# Buttons
    # Quit button
    font0 = pygame.font.SysFont('Ariel',70)
    surf0 = font0.render('Quit', True, 'black')
    exitButton = pygame.Rect(1180,10,110,60)

    # Upgrade Bar 1 button
    font1 = pygame.font.SysFont('Ariel',50,bold=False)
    surf1 = font1.render('Upgrade', True, 'white')
    up1Button = pygame.Rect(1100,300,150,50)
    up1Price = 0.0 #then go to 300.0

    # Upgrade Bar 2 button
    font2 = pygame.font.SysFont('Ariel',50,bold=False)
    surf2 = font2.render('Upgrade', True, 'white')
    up2Button = pygame.Rect(1100,450,150,50)
    up2Price = 500.0

    # Upgrade Bar 3 button
    font3 = pygame.font.SysFont('Ariel',50,bold=False)
    surf3 = font3.render('Upgrade', True, 'white')
    up3Button = pygame.Rect(1100,600,150,50)
    up3Price = 700.0

    # Display Upgrade Bar 1 Price
    up1PriceDisplay = pygame.font.SysFont('Ariel',40)
    def displayup1Price (up1Price):
         up1Price = up1PriceDisplay.render("$" + str(up1Price), True, (0,0,0))
         screen.blit(up1Price, (1100,355))

    # Display Upgrade Bar 2 Price
    up2PriceDisplay = pygame.font.SysFont('Ariel',40)
    def displayup2Price (up2Price):
         up2Price = up2PriceDisplay.render("$" + str(up2Price), True, (0,0,0))
         screen.blit(up2Price, (1100,505))

    # Display Upgrade Bar 3 Price
    up3PriceDisplay = pygame.font.SysFont('Ariel',40)
    def displayup3Price (up3Price):
         up3Price = up3PriceDisplay.render("$" + str(up3Price), True, (0,0,0))
         screen.blit(up3Price, (1100,655))

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- GAME RUN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    #Run the events in game
    gamerun = True
    ticknum = 60#60 fps
    while gamerun:

        for event in pygame.event.get():

            # Check if player quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Check if player meets goal
            if user_money >= money_goal:
                #TODO return a win screen with final score
                #close game after a pause
                pygame.time.delay(2628000000)#delays for 1 real life month
                #tried setting the tick to a ridiculously high and low number
                #DO NOT DO THAT
                #It did not solve the issue but created lots of issues
                Final_Time = pygame.time.Clock.get_time(CLOCK)
                fontFT = pygame.font.SysFont('Ariel',80,bold=False)
                surfFT = fontFT.render("Final Time: " + str(Final_Time), True, 'blueviolet')
                screen.blit(surfFT, (screen_width/5, screen_height/2))             
                #gamerun = False
    
            
            # Display Money and Timer
            blitScoreboard(screen, screen_width, screen_height)
            user_money = round(user_money, 2)
            displayMoney(user_money)
            #TODO Timer should start AFTER entering name and color
            #displayTimer()

            # Display value of each loading bar
            displayL1Value(L1Value)
            displayL2Value(L2Value)
            displayL3Value(L3Value)

            # Display Upgrade Bar Prices
            blitUpPrices(screen)
            up1Price = round(up1Price, 2)
            displayup1Price(up1Price)
            up2Price = round(up2Price, 2)
            displayup2Price(up2Price)
            up3Price = round(up3Price, 2)
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
                                 up1Price = 300.0
                                 displayTimer()
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
                            else:
                                L3_speed *= 1.3
                            user_money -= up3Price
                            up3Price *= 1.2

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
        a,b = pygame.mouse.get_pos()
        if up1Button.x <= a <= up1Button.x + 150 and up1Button.y <= b <= up1Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up1Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up1Button)
        screen.blit(surf1,(up1Button.x+5, up1Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------        
        # Upgrade Bar 2 button
        a,b = pygame.mouse.get_pos()
        if up2Button.x <= a <= up2Button.x + 150 and up2Button.y <= b <= up2Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up2Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up2Button)
        screen.blit(surf2,(up2Button.x+5, up2Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------        
        # Upgrade Bar 3 button
        a,b = pygame.mouse.get_pos()
        if up3Button.x <= a <= up3Button.x + 150 and up3Button.y <= b <= up3Button.y + 50:
            pygame.draw.rect(screen,(100,100,100),up3Button)
        else:
            pygame.draw.rect(screen,(0,0,0),up3Button)
        screen.blit(surf3,(up3Button.x+5, up3Button.y+5))
#-------------------------------------------------------------------------------------------------------------------------------
        #Loading Bar Animations

        # Loading bar 1
        L1_xpos += L1_speed            
        if L1_xpos > load_limit:
            
            user_money += L1_Amt
            L1_xpos = start_x
            
            pygame.draw.rect(screen, 'white', (L1_xpos, L1_ypos, 740, bar_height))
        screen.blit(L1_Bar,(L1_xpos,L1_ypos))
        
        # Loading bar 2
        L2_xpos += L2_speed
        if L2_xpos > load_limit:
            
            user_money += L2_Amt
            L2_xpos = start_x
            
            pygame.draw.rect(screen, 'white', (L2_xpos, L2_ypos, 740, bar_height))
        screen.blit(L2_Bar,(L2_xpos,L2_ypos))

        # Loading bar 3
        L3_xpos += L3_speed
        if L3_xpos > load_limit:
            
            user_money += L3_Amt
            L3_xpos = start_x
            

            pygame.draw.rect(screen, 'white', (L3_xpos, L3_ypos, 740, bar_height))
        screen.blit(L3_Bar,(L3_xpos,L3_ypos))
#-------------------------------------------------------------------------------------------------------------------------------
        
        pygame.display.update()
        CLOCK.tick(ticknum)#cap framerate at 60 fps     

    pygame.quit()
    exit()