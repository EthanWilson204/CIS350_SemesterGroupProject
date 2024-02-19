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
import Screen
import pygame

#initialize pygame
pygame.init()
CLOCK = pygame.time.Clock()

if __name__ == "__main__":

    #main display
    screen_width = 1600
    screen_height = 900
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill('Tan')
    pygame.display.set_caption("Main Game")

    #define start and end for bars
    start_x = 320
    load_limit = 1000

    #define bar positions
    L1_xpos = start_x
    L1_ypos = 325
    L2_xpos = start_x
    L2_ypos = 425
    L3_xpos = start_x
    L3_ypos = 525
    bar_length = 50
    bar_height = 50


    #define bar speeds
    L1_speed = 2
    L2_speed = 3
    L3_speed = 4

    Screen.SetBackground(screen, load_limit, screen_width, screen_height,L1_xpos,L2_xpos,L3_xpos,L1_ypos,L2_ypos,L3_ypos)

    #loading bar 1
    L1_Bar = pygame.Surface((bar_length,bar_height))
    L1_Bar.fill('black')

    #loading bar 2
    L2_Bar = L1_Bar.copy()
    L2_Bar.fill('blue')

    #loading bar 3
    L3_Bar = L1_Bar.copy()
    L3_Bar.fill('green')

    #Define money variables
    money_goal = 1000 #$1,000,000,000
    user_money = 0
    L1_Amt = 100
    L2_Amt = 200
    L3_Amt = 300

    #Run the events in game
    gamerun = True
    while gamerun:

        #check if player quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if user_money >= money_goal:
                gamerun = False

        #loading bar 1
        #animate bar moving
        L1_xpos += L1_speed
        if user_money == money_goal:
                L1_xpos = start_x
                
        if L1_xpos > load_limit:
            L1_xpos = start_x
            user_money += L1_Amt
            
            pygame.draw.rect(screen, 'tan', (L1_xpos, L1_ypos, 750, bar_height))
        screen.blit(L1_Bar,(L1_xpos,L1_ypos))
        
        #loading bar 2
        #animate bar moving
        L2_xpos += L2_speed
        if L2_xpos > load_limit:
            L2_xpos = start_x
            user_money += L2_Amt
            
            pygame.draw.rect(screen, 'tan', (L2_xpos, L2_ypos, 750, bar_height))
        screen.blit(L2_Bar,(L2_xpos,L2_ypos))

        #loading bar 3
        #animate bar moving
        L3_xpos += L3_speed
        if L3_xpos > load_limit:
            L3_xpos = start_x
            user_money += L3_Amt
            

            pygame.draw.rect(screen, 'tan', (L3_xpos, L3_ypos, 750, bar_height))
        screen.blit(L3_Bar,(L3_xpos,L3_ypos))
        
        pygame.display.update()
        CLOCK.tick(60)     

    pygame.quit()

