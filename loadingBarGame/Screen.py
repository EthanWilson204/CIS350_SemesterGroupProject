import pygame

def SetBackground(screen, screen_width, screen_height, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos):
    
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

def blitUpPrices(screen):
    pygame.draw.rect(screen, 'dark grey', (1100, 355, 300, 100))
    pygame.draw.rect(screen, 'dark grey', (1100, 505, 300, 100))
    pygame.draw.rect(screen, 'dark grey', (1100, 655, 300, 100))

def blitStartup(screen):
    #Profile setup menu
    Profile_Menu = pygame.Surface((1050,550))
    Profile_Menu.fill((200,200,200))
    screen.blit(Profile_Menu, (250,200))

