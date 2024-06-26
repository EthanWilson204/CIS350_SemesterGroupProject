'''
Project: Millionaire Tycoon
Class: CIS 350-02
Professor: J. Nandigham
Authors: Gabe Kucinich, Gideon Moerdyk, Ethan Wilson

Description:
A game where you load bars to earn money towards a total. Everytime a bar loads, money is added to the total.
You can spend money to upgrade the speed of each bar to earn money faster. Watch out for randomized taxes! Purchase status effects to 
multiply income or reduce taxes. Once the total is reached, the gameis complete and a time will be displayed showing how fast it was 
completed. Figure out how to beat the game as fast as possible.
'''
# Imports
import pygame
from sys import exit
from Screen import *
from GameFunctions import *

# Initialize pygame
pygame.init()
CLOCK = pygame.time.Clock()

#-------------------------------------------------------------------------------------------------------------------------------
# Initialize fonts
barValueDisplay = pygame.font.SysFont('Ariel',40)
congratsFont = pygame.font.SysFont('Ariel',150)
gameOverFont = pygame.font.SysFont('Ariel',80)
moneyDisplay = pygame.font.SysFont('Ariel',100)
muteFont = pygame.font.SysFont('Ariel',40)
optionFont = pygame.font.SysFont('Ariel',40,)
purchaseFont  = pygame.font.SysFont('Ariel',45)
quitFont = pygame.font.SysFont('Ariel',70)
status1Font = pygame.font.SysFont('Ariel',50)
status2Font = pygame.font.SysFont('Ariel',46)
status3Font = pygame.font.SysFont('Ariel',50)
statusPriceDisplay = pygame.font.SysFont('Ariel',30)
up1PriceDisplay = pygame.font.SysFont('Ariel',40)
up2PriceDisplay = pygame.font.SysFont('Ariel',40)
up3PriceDisplay = pygame.font.SysFont('Ariel',40)
upgradeFont = pygame.font.SysFont('Ariel',50)
userLetterFont = pygame.font.SysFont('Ariel',250)
timerFont = pygame.font.SysFont('Ariel', 100)
titleFont = pygame.font.SysFont('Ariel',70, bold = True)

#-------------------------------------------------------------------------------------------------------------------------------
# Sound Effects
soundOn = True
victorySFX = False
purchase_sfx = pygame.mixer.Sound("sfx/purchase.mp3")
status_sfx = pygame.mixer.Sound("sfx/status.mp3")
statusEnd_sfx = pygame.mixer.Sound("sfx/statusEnd.mp3")
tax_sfx = pygame.mixer.Sound("sfx/taxes.mp3")
victory_sfx = pygame.mixer.Sound("sfx/victory.mp3")

#-------------------------------------------------------------------------------------------------------------------------------
# Game Over
def displayGameOver(game_time):
    congrats1 = congratsFont.render("Congratulations!", True, (0,200,0))
    congrats2 = gameOverFont.render("You reached $1,000,000 in", True, (0,0,0))
    congrats3 = gameOverFont.render(str(game_time) + " seconds.", True, (0,0,0))
    congrats4 = optionFont.render("Thanks for playing!", True, (255,0,0))
    screen.blit(congrats1, (340,210))
    screen.blit(congrats2, (425,370))
    screen.blit(congrats3, (630,430))
    screen.blit(congrats4, (645,600))

#-------------------------------------------------------------------------------------------------------------------------------
# Display Timer
def displayTimer():
    timerSurf = timerFont.render("Time: " + str(game_time), True, 'white')
    screen.blit(timerSurf, (800,70))

# Display L1 Value
def displayL1Value(L1Value):
    L1Value = barValueDisplay.render("$" + str(L1Value), True, (0,0,0))
    screen.blit(L1Value, (660,360))

# Display L2 Value
def displayL2Value(L2Value):
    L2Value = barValueDisplay.render("$" + str(L2Value), True, (0,0,0))
    screen.blit(L2Value, (660,510))

# Display L3 Value
def displayL3Value(L3Value):
    L3Value = barValueDisplay.render("$" + str(L3Value), True, (0,0,0))
    screen.blit(L3Value, (660,660))

# Display Money
def displayMoney (money):
    moneyComma = (f"{money:,}")
    moneyComma = moneyDisplay.render("$" + moneyComma, True, (255,255,255))
    screen.blit(moneyComma, (300,70))

# Display Status 1 Price
def displaystatus1Price(status1Price):
    status1Price = statusPriceDisplay.render("$" + str(status1Price), True, (255,255,255))
    screen.blit(status1Price, (80,305))

# Display Status 2 Price
def displaystatus2Price(status2Price):
    status2Price = statusPriceDisplay.render("$" + str(status2Price), True, (255,255,255))
    screen.blit(status2Price, (80,455))

# Display Status 3 Price
def displaystatus3Price(status3Price):
    status3Price = statusPriceDisplay.render("$" + str(status3Price), True, (255,255,255))
    screen.blit(status3Price, (80,605))

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

# Display Title
def displayTitle():
    millionaire = titleFont.render("Millionaire", True, (0,200,0))
    tycoon = titleFont.render("Tycoon", True, (255,255,255))
    screen.blit(millionaire, (2,60))
    screen.blit(tycoon, (35,100))

#-------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    
    # Main Display
    screen_width = 1300
    screen_height = 750
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill('Dark Grey')
    pygame.display.set_caption("Main Game")

    #define start and end for bars
    start_x = 320
    load_limit = 1000

    #define if taxes are on, tax value, and percentage of money taken from taxes
    taxesOn = True
    taxVal = 999
    taxPercent = 50

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

    # Draw buttons
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
    #Bar 1
    L1_Bar = pygame.Surface((bar_length,bar_height))
    L1_Bar.fill('red')
    L1Value = 100
    L1BarColor = "white"

    #Bar 2
    L2_Bar = L1_Bar.copy()
    L2_Bar.fill('green')
    L2Value = 200
    L2BarColor = "white"  

    #Bar 3
    L3_Bar = L1_Bar.copy()
    L3_Bar.fill('blue')
    L3Value = 300
    L3BarColor = "white"
    
#-------------------------------------------------------------------------------------------------------------------------------
# Money System
    # Define money variables
    money_goal = 1000000 #$1,000,000
    user_money = 0
    L1_Amt = 100
    L2_Amt = 200
    L3_Amt = 300

#-------------------------------------------------------------------------------------------------------------------------------
# Buttons
    # Quit button
    quitSurf = quitFont.render('Quit', True, 'black')
    exitButton = pygame.Rect(1180,10,110,60)

    # Mute button
    muteSurf = muteFont.render('Sound', True, 'black')
    muteButton = pygame.Rect(1195,80,95,40)

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

    # Status Buttons
    #Status 1
    status1Surf = status1Font.render('Profit x2', True, 'white')
    cooldownStatus1Surf = status1Font.render(' Active!', True, 'white')
    status1Button = pygame.Rect(50,250,150,50)
    status1Price = 50000
    status1_active = False
    stat1_limit = 0

    #Status 2
    status2Surf = status2Font.render('No Taxes', True, 'white')
    cooldownStatus2Surf = status2Font.render(' Active!', True, 'white')
    status2Button = pygame.Rect(50,400,150,50)
    status2Price = 100000
    status2Active = False
    stat2_limit = 0

    #Status 3
    status3Surf = status3Font.render('Tax Cut', True, 'white')
    status3Button = pygame.Rect(50,550,150,50)
    status3Price = 1000

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- GAME RUN -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    # Set up timer
    game_time = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    # Run the events in game
    gamerun = True
    ticknum = 60 #60 fps

    # Within the game loop
    while gamerun:
        
    # Display Money and Timer
        blitScoreboard(screen, screen_width, screen_height)
        user_money = round(user_money, 0)
        displayMoney(user_money)
        displayTimer()

    # Display price of each status effect
        displaystatus1Price(status1Price)
        displaystatus2Price(status2Price)
        displaystatus3Price(status3Price)

    # Display value of each loading bar
        displayL1Value(L1Value)
        displayL2Value(L2Value)
        displayL3Value(L3Value)

    # Display game title
        displayTitle()

    # Taxes, apply a tax on money so long as the player has not won the game, has money to tax and taxes are on
        if user_money < money_goal and user_money > 0.0 and taxesOn:
            #set the user_money equal to the returned taxed value based on RNG
            user_money = taxes(user_money, taxVal, taxPercent, tax_sfx, soundOn)#have a taxVal chance for taxes each tick


     # Check if player meets goal
        if user_money >= money_goal:
            
            # Stop bars from loading and stop earning more money once game is won
            L1_speed, L2_speed, L3_speed, user_money = 0, 0, 0, 1000000

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

            # Mute button
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if muteButton.collidepoint(event.pos):
                        if soundOn == True:
                            soundOn = False
                        else:
                            soundOn = True

            # Upgrade Bar 1 button
            if user_money >= up1Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up1Button.collidepoint(event.pos):    
                            if user_money < 1000000:

                                if soundOn == True:
                                    purchase_sfx.play()
                                if L1_speed == 0:
                                    L1_speed = 3.0
                                    up1Price = 300
                                else:
                                    components = [L1_speed, up1Price, user_money] 
                                    L1_speed, up1Price, user_money = Upgrade_Bar(components)

            # Upgrade Bar 2 button
            if user_money >= up2Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up2Button.collidepoint(event.pos):
                            if user_money < 1000000:

                                if soundOn == True:
                                    purchase_sfx.play()
                                if L2_speed == 0:
                                    L2_speed = 1.5
                                    up2Price = 500
                                    user_money -= 1000
                                else:
                                    components = [L2_speed, up2Price, user_money] 
                                    L2_speed, up2Price, user_money = Upgrade_Bar(components)

            # Upgrade Bar 3 button
            if user_money >= up3Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if up3Button.collidepoint(event.pos):
                            if user_money < 1000000:  

                                if soundOn == True:
                                    purchase_sfx.play()
                                if L3_speed == 0:
                                    L3_speed = 0.75
                                    up3Price = 700
                                    user_money -= 2000
                                else:
                                    components = [L3_speed, up3Price, user_money] 
                                    L3_speed, up3Price, user_money = Upgrade_Bar(components)


            # Status 1 button
            if status1_active == False:
                if user_money >= status1Price:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if status1Button.collidepoint(event.pos):
                                if user_money < 1000000:
                        
                                    if soundOn == True:
                                        status_sfx.play()
                            
                                    #status components in tuple to make them references
                                    amount_comps = [L1_Amt, L2_Amt, L3_Amt, user_money, status1_active, status1Price]

                                    #upgrade the speed, take away money, and set status active to be true
                                    L1_Amt, L2_Amt, L3_Amt, user_money, status1_active, status1Price = Start_Profit(amount_comps, 2)
                                    stat1_limit = int(game_time) + 10
                                    status1Price *= 1.4
                                    status1Price = round(status1Price, 0)
            

            if status1_active == True:
                if int(game_time) >= stat1_limit:
                    
                    if soundOn == True:
                        statusEnd_sfx.play()
                    
                    stop_comps = [L1_Amt, L2_Amt, L3_Amt, status1_active]
                    L1_Amt, L2_Amt, L3_Amt, status1_active = Stop_Profit(stop_comps, 2)
               
            # Status 2 button
            if status2Active == False:
                if user_money >= status2Price:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if status2Button.collidepoint(event.pos):
                            if user_money < 1000000:
                                if soundOn == True:
                                    status_sfx.play()
                                
                                user_money -= status2Price
                                status2Active = True
                                stat2_limit = int(game_time) + 20
                                taxesOn = False

            if status2Active == True:
                if int(game_time) >= stat2_limit:
                    
                    if soundOn == True:
                        statusEnd_sfx.play()
                    
                    status2Active = False
                    taxesOn = True

            # Status 3 button
            if user_money >= status3Price:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if status3Button.collidepoint(event.pos):
                        if user_money < 1000000:        
                            if soundOn == True:
                                status_sfx.play()
                            
                            
                            user_money -= status3Price
                            taxPercent -= 2
                            status3Price *= 1.3
                            status3Price = round(status3Price, 0)

#-------------------------------------------------------------------------------------------------------------------------------
    # Exit button
        a,b = pygame.mouse.get_pos()
        if exitButton.x <= a <= exitButton.x + 110 and exitButton.y <= b <= exitButton.y + 60:
            pygame.draw.rect(screen,(255,25,25),exitButton)
        else:
            pygame.draw.rect(screen,(200,0,0),exitButton)
        screen.blit(quitSurf,(exitButton.x+5, exitButton.y+5))  
#-------------------------------------------------------------------------------------------------------------------------------
    # Mute button
        a,b = pygame.mouse.get_pos()
        if soundOn == True:
            if muteButton.x <= a <= muteButton.x + 95 and muteButton.y <= b <= muteButton.y + 40:
                pygame.draw.rect(screen,(25,255,25),muteButton)
            else:
                pygame.draw.rect(screen,(0,200,0),muteButton)
            screen.blit(muteSurf,(muteButton.x+5, muteButton.y+5))
        else:
            if muteButton.x <= a <= muteButton.x + 95 and muteButton.y <= b <= muteButton.y + 40:
                pygame.draw.rect(screen,(255,25,25),muteButton)
            else:
                pygame.draw.rect(screen,(200,0,0),muteButton)
            screen.blit(muteSurf,(muteButton.x+5, muteButton.y+5))

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
        if status1_active == False:
            if status1Button.x <= a <= status1Button.x + 150 and status1Button.y <= b <= status1Button.y + 50:
                pygame.draw.rect(screen,(150,0,0),status1Button)
            else:
                pygame.draw.rect(screen,(200,0,0),status1Button)
            screen.blit(status1Surf,(status1Button.x+5, status1Button.y+5))
        else:
            pygame.draw.rect(screen,(0,200,0),status1Button)
            screen.blit(cooldownStatus1Surf,(status1Button.x+5, status1Button.y+5))

#-------------------------------------------------------------------------------------------------------------------------------
    # Status 2 button    
        if status2Active == False:
            if status2Button.x <= a <= status2Button.x + 150 and status2Button.y <= b <= status2Button.y + 50:
                pygame.draw.rect(screen,(150,0,0),status2Button)
            else:
                pygame.draw.rect(screen,(200,0,0),status2Button)
            screen.blit(status2Surf,(status2Button.x+5, status2Button.y+5))
        else:
            pygame.draw.rect(screen,(0,200,0),status2Button)
            screen.blit(cooldownStatus2Surf,(status2Button.x+5, status2Button.y+5))

#-------------------------------------------------------------------------------------------------------------------------------
    # Status 3 button    
        if status3Button.x <= a <= status3Button.x + 150 and status3Button.y <= b <= status3Button.y + 50:
            pygame.draw.rect(screen,(75,75,150),status3Button)
        else:
            pygame.draw.rect(screen,(75,75,200),status3Button)
        screen.blit(status3Surf,(status3Button.x+5, status3Button.y+5))

#-------------------------------------------------------------------------------------------------------------------------------
    #Loading Bar Animations
        # Loading bar 1
        L1_xpos += L1_speed
        L2_xpos += L2_speed
        L3_xpos += L3_speed
                
        if L1_xpos > load_limit:
            user_money, L1_xpos = Add_Reset(L1_Amt, L1_xpos, start_x, user_money)
            pygame.draw.rect(screen, L1BarColor, (L1_xpos, L1_ypos, 740, bar_height))
        
        if L1_speed >= 50:
            L1BarColor = "red"
        
        # Loading bar 2
        if L2_xpos > load_limit:
            user_money, L2_xpos = Add_Reset(L2_Amt, L2_xpos, start_x, user_money)
            pygame.draw.rect(screen, L2BarColor, (L2_xpos, L2_ypos, 740, bar_height))

        if L2_speed >= 50:
            L2BarColor = "green"

        # Loading bar 3
        if L3_xpos > load_limit:
            user_money, L3_xpos = Add_Reset(L3_Amt, L3_xpos, start_x, user_money)
            pygame.draw.rect(screen, L3BarColor, (L3_xpos, L3_ypos, 740, bar_height))

        if L3_speed >= 50:
            L3BarColor = "blue"
            
        screen.blit(L1_Bar,(L1_xpos,L1_ypos))
        screen.blit(L2_Bar,(L2_xpos,L2_ypos))
        screen.blit(L3_Bar,(L3_xpos,L3_ypos))

        if user_money >= money_goal:
            blitStartup(screen)
            displayGameOver(game_time)
            
            if soundOn == True:
                if victorySFX == False:
                    victory_sfx.play()
                    victorySFX = True
            
#-------------------------------------------------------------------------------------------------------------------------------
        pygame.display.update()
        CLOCK.tick(ticknum)#cap framerate at 60 fps    
    #pygame.quit()
    #exit()
