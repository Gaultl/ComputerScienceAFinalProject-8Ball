import pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((903, 490))
background = pygame.image.load("Pool-Table.png")
# background = pygame.transform.scale(background, (903, 490))
running = True

#pool cue?
# class Cue():
#     def __init__(self, pos):
#         cue_image = pygame.image.load("Pool-Cue.png").convert_alpha()
#         self.image = cue_image
#         self.angle = 0
#         self.new_image = pygame.transform.rotate(self.image, self.angle)
#         self.rect = self.image.get_rect()
#         self.rect.center = pos


while running:
    screen.blit(background, (0, 0))
    cue = pygame.image.load("Pool-Cue.png").convert_alpha()
    screen.blit(cue, (200, 200))
    angle = 0
    keys = pygame.key.get_pressed()

    angle += 50
    pygame.transform.rotate(cue, angle)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
