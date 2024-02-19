'''
Python Project CIS350

'''
#imports
import GameScreen
import pygame
from sys import exit


#initialize pygame
pygame.init()

#fps control
CLOCK = pygame.time.Clock()

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

#define bar speeds
L1_speed = 2
L2_speed = 3
L3_speed = 4


bar_length = 50
bar_height = 50

GameScreen.SetBackground(screen, load_limit, screen_width, screen_height,L1_xpos,L2_xpos,L3_xpos,L1_ypos,L2_ypos,L3_ypos)

#loading bar 1
L1_Bar = pygame.Surface((bar_length,bar_height))
L1_Bar.fill('black')

#loading bar 2
L2_Bar = L1_Bar.copy()
L2_Bar.fill('blue')

#loading bar 3
L3_Bar = L1_Bar.copy()
L3_Bar.fill('green')


#Run the events in game
while True:

    #check if player quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    #loading bar 1
    L1_xpos += L1_speed
    if L1_xpos > load_limit:
        L1_xpos = start_x
        pygame.draw.rect(screen, 'tan', (L1_xpos, L1_ypos, 750, bar_height))
    
    screen.blit(L1_Bar,(L1_xpos,L1_ypos))
    
    #loading bar 2
    L2_xpos += L2_speed
    if L2_xpos > load_limit:
        L2_xpos = start_x
        pygame.draw.rect(screen, 'tan', (L2_xpos, L2_ypos, 750, bar_height))
    
    screen.blit(L2_Bar,(L2_xpos,L2_ypos))
    
    #loading bar 3
    L3_xpos += L3_speed
    if L3_xpos > load_limit:
        L3_xpos = start_x
        pygame.draw.rect(screen, 'tan', (L3_xpos, L3_ypos, 750, bar_height))
    
    screen.blit(L3_Bar,(L3_xpos,L3_ypos))
    
    pygame.display.update()
    CLOCK.tick(60)     

pygame.quit()

