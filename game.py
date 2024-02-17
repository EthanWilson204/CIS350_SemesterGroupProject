import pygame, sys, threading
from pygame.locals import *
pygame.init()


screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Loading Bar")

FONT = pygame.font.SysFont("Roboto", 100)
CLOCK = pygame.time.Clock()

#player = pygame.Rect((300, 250, 50, 50))
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
    screen.fill("#5592aa")      
        
    pygame.display.update()
    CLOCK.tick(60)     

pygame.quit()
