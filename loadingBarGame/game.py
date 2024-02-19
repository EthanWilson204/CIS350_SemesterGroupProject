import pygame
from sys import exit
#initialize pygame
pygame.init()

#fps control
CLOCK = pygame.time.Clock()

#display
screen = pygame.display.set_mode((1600,900))
screen.fill('Tan')
pygame.display.set_caption("Loading Bar")

#surface (screen overlay) displays

#start position for all bars
start_x = 320
load_limit = 1000
bar_length = 50
bar_height = 50

#loading bar 1
L1_xpos = start_x
L1_ypos = 325
L1_Bar = pygame.Surface((bar_length,bar_height))
L1_Bar.fill('black')
L1_speed = 1

#loading bar 2
L2_xpos = start_x
L2_ypos = 425
L2_Bar = L1_Bar.copy()
L2_Bar.fill('blue')
L2_speed = 2

#loading bar 3
L3_xpos = start_x
L3_ypos = 525
L3_Bar = L1_Bar.copy()
L3_Bar.fill('green')
L3_speed = 3

#button background
upgrade1_button_background = pygame.Surface((bar_length + 100, bar_height+30))
upgrade2_button_background = pygame.Surface((bar_length + 100, bar_height+30))
upgrade3_button_background = pygame.Surface((bar_length + 100, bar_height+30))


#Run the events in game
while True:

    #check if player quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
    
    screen.blit(upgrade1_button_background,(load_limit + 100, L1_ypos - 15))
    screen.blit(upgrade2_button_background,(load_limit + 100, L2_ypos - 15))
    screen.blit(upgrade3_button_background,(load_limit + 100, L3_ypos - 15))
    
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




'''
#loading bar background
#coords for the top left corners of the backgrounds for each loading bar (BGQ# specifies quadrant)
LOADING_BGQ1 = pygame.draw.rect(screen, ("RED"), (x_coord_Q1Q4, y_coord_Q1Q2-200, bar_width, bar_height))
LOADING_BGQ2 = pygame.draw.rect(screen, ("RED"), (x_coord_Q2Q3, y_coord_Q1Q2-200, bar_width, bar_height))
LOADING_BGQ3 = pygame.draw.rect(screen, ("RED"), (x_coord_Q1Q4, y_coord_Q3Q4, bar_width,bar_height))
LOADING_BGQ4 = pygame.draw.rect(screen, ("RED"), (x_coord_Q2Q3, y_coord_Q3Q4, bar_width,bar_height))

#upgrade button background
LOADING_BGQ1 = pygame.draw.rect(screen, ("BLUE"), (x_coord_Q1Q4 + bar_width + 30, y_coord_Q1Q2-200, 100, bar_height))
LOADING_BGQ2 = pygame.draw.rect(screen, ("BLUE"), (x_coord_Q2Q3 + bar_width + 30, y_coord_Q1Q2-200, 100, bar_height))
LOADING_BGQ3 = pygame.draw.rect(screen, ("BLUE"), (x_coord_Q1Q4 + bar_width + 30, y_coord_Q3Q4, 100, bar_height))
LOADING_BGQ4 = pygame.draw.rect(screen, ("BLUE"), (x_coord_Q2Q3 + bar_width + 30, y_coord_Q3Q4, 100, bar_height))
'''
