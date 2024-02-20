import pygame
from GameFunctions import TextDisplay

def SetBackground(screen, screen_width, screen_height, B1_surf, B2_surf, B3_surf, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos):
    
    #surface (screen overlay) displays
    
    #start position for all bars
   
    #bar background
    pygame.draw.rect(screen, 'red', (L1_xpos-15, L1_ypos-15, 780, 80))
    pygame.draw.rect(screen, 'red', (L2_xpos-15, L2_ypos-15, 780, 80))
    pygame.draw.rect(screen, 'red', (L3_xpos-15, L3_ypos-15, 780, 80))
    pygame.draw.rect(screen, 'tan', (L1_xpos, L1_ypos, 740, 50))
    pygame.draw.rect(screen, 'tan', (L2_xpos, L2_ypos, 740, 50))
    pygame.draw.rect(screen, 'tan', (L3_xpos, L3_ypos, 740, 50))

    #button backbgrounds
    pygame.draw.rect(screen, "blue", (1100, L1_ypos - 15, 150, 80))
    pygame.draw.rect(screen, "blue", (1100, L2_ypos - 15, 150, 80))
    pygame.draw.rect(screen, "blue", (1100, L3_ypos - 15, 150, 80))
    
    #draw buttons
    screen.blit(B1_surf,(1103, L1_ypos))
    screen.blit(B2_surf,(1103, L2_ypos))
    screen.blit(B3_surf,(1103, L3_ypos))
    
    #draw texts
    btext_font = pygame.font.SysFont(None, 30)
    TextDisplay(screen, "Upgrade Bar 1", btext_font, 1104, L1_ypos + 15)
    TextDisplay(screen, "Upgrade Bar 2", btext_font, 1104, L2_ypos + 15)
    TextDisplay(screen, "Upgrade Bar 3", btext_font, 1104, L3_ypos + 15)

    #upper bar display
    Profile_Bar = pygame.Surface((screen_width, 200))
    Profile_Bar.fill((160, 160, 160))


    #left side status bar display
    Left_Side_Bar = pygame.Surface((250, screen_height - 200))
    Left_Side_Bar.fill((101, 132, 129))


    #profile corner display
    Profile_Corner = pygame.Surface((250,200))
    Profile_Corner.fill((176, 98, 108))


    #static screen behavior    
    screen.blit(Profile_Bar, (0,0))
    screen.blit(Profile_Corner, (0,0))
    screen.blit(Left_Side_Bar, (0,200))
