import pygame, sys, threading
from pygame.locals import *
#initialize pygame
pygame.init()

#display
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Loading Bar")

#font
FONT = pygame.font.SysFont("Roboto", 100)

#fps
CLOCK = pygame.time.Clock()

#player = pygame.Rect((300, 250, 50, 50))


#Run the events in game
while True:
    
    #check to see if player quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
    
    #screen background   
    screen.fill("WHITE")      
        
    #keep the game running. Run at 60 fps

    #    CLOCK.tick(60)     

    WORK = 10000

    #loading bar background
    #coords for the top left corners of the backgrounds for each loading bar (BGQ# specifies quadrant)
    LOADING_BGQ1 = pygame.draw.rect(screen, ("RED"), (220,130,200,100))
    LOADING_BGQ2 = pygame.draw.rect(screen, ("RED"), (860,130,200,100))
    LOADING_BGQ3 = pygame.draw.rect(screen, ("RED"), (860,490,200,100))
    LOADING_BGQ4 = pygame.draw.rect(screen, ("RED"), (220,490,200,100))
    
    
    

    pygame.display.update()

pygame.quit()
sys.quit()