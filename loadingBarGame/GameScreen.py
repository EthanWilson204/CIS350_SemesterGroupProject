import pygame

def SetBackground(screen, load_limit, screen_width, screen_height, L1_xpos, L2_xpos, L3_xpos, L1_ypos, L2_ypos, L3_ypos):
    
    #surface (screen overlay) displays
    
    #start position for all bars
    bar_length = 50
    bar_height = 50    

    #bar background
    pygame.draw.rect(screen, 'red', (L1_xpos-15, L1_ypos-15, 780, bar_height+30))
    pygame.draw.rect(screen, 'red', (L2_xpos-15, L2_ypos-15, 780, bar_height+30))
    pygame.draw.rect(screen, 'red', (L3_xpos-15, L3_ypos-15, 780, bar_height+30))
    pygame.draw.rect(screen, 'tan', (L1_xpos, L1_ypos, 740, bar_height))
    pygame.draw.rect(screen, 'tan', (L2_xpos, L2_ypos, 740, bar_height))
    pygame.draw.rect(screen, 'tan', (L3_xpos, L3_ypos, 740, bar_height))


    #button background
    '''
    upgrade1_button_background = pygame.Surface((bar_length + 100, bar_height+30))
    upgrade2_button_background = pygame.Surface((bar_length + 100, bar_height+30))
    upgrade3_button_background = pygame.Surface((bar_length + 100, bar_height+30))
    B1_rect = upgrade1_button_background.get_rect(topleft = (load_limit + 100, L1_ypos - 15))
    B2_rect = upgrade2_button_background.get_rect(topleft = (load_limit + 100, L2_ypos - 15))
    B3_rect = upgrade3_button_background.get_rect(topleft = (load_limit + 100, L3_ypos - 15))
    '''
    
    #button backbgrounds
    pygame.draw.rect(screen, "black", (load_limit + 100, L1_ypos - 15,bar_length + 100, bar_height+30))
    pygame.draw.rect(screen, "black", (load_limit + 100, L2_ypos - 15,bar_length + 100, bar_height+30))
    pygame.draw.rect(screen, "black", (load_limit + 100, L3_ypos - 15,bar_length + 100, bar_height+30))
    
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
