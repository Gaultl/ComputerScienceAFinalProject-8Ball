import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((976, 530))
background = pygame.image.load("Pool-Table.png")
background = pygame.transform.scale(background, (976, 530))
running = True

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
