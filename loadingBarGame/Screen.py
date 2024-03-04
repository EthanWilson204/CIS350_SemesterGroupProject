import pygame
from GameFunctions import TextDisplay

def SetBackground(screen, screen_width, screen_height, B1_surf, B2_surf, B3_surf, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos):
    
    #surface (screen overlay) displays
    
    #start position for all bars
   
    #bar background
    pygame.draw.rect(screen, 'black', (L1_xpos-5, L1_ypos-5, 750, 60))
    pygame.draw.rect(screen, 'black', (L2_xpos-5, L2_ypos-5, 750, 60))
    pygame.draw.rect(screen, 'black', (L3_xpos-5, L3_ypos-5, 750, 60))
    pygame.draw.rect(screen, 'white', (L1_xpos, L1_ypos, 740, 50))
    pygame.draw.rect(screen, 'white', (L2_xpos, L2_ypos, 740, 50))
    pygame.draw.rect(screen, 'white', (L3_xpos, L3_ypos, 740, 50))

    #upper bar display
    Profile_Bar = pygame.Surface((screen_width, 200))
    Profile_Bar.fill((10,60,0))


    #left side status bar display
    Left_Side_Bar = pygame.Surface((250, screen_height - 200))
    Left_Side_Bar.fill((10, 60, 0))


    #profile corner display
    Profile_Corner = pygame.Surface((250,200))
    Profile_Corner.fill((0,0,0))


    #static screen behavior    
    screen.blit(Profile_Bar, (0,0))
    screen.blit(Profile_Corner, (0,0))
    screen.blit(Left_Side_Bar, (0,200))

def blitScoreboard(screen, screen_width, screen_height):
    #upper bar display
    Profile_Bar = pygame.Surface((screen_width, 200,))
    Profile_Bar.fill((10,60,0))


    #left side status bar display
    Left_Side_Bar = pygame.Surface((250, screen_height - 200))
    Left_Side_Bar.fill((10, 60, 0))


    #profile corner display
    Profile_Corner = pygame.Surface((250,200))
    Profile_Corner.fill((0,0,0))


    #static screen behavior    
    screen.blit(Profile_Bar, (0,0))
    screen.blit(Profile_Corner, (0,0))
    screen.blit(Left_Side_Bar, (0,200))