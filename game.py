
import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((700,400))

while True:
    screen.fill(("tan"))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

        pygame.display.update()