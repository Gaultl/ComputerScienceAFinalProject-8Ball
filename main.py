import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((903, 490))
background = pygame.image.load("Pool-Table.png")

running = True

image = pygame.image.load("Pool-Cue.png")
mov_image = pygame.image.load("Pool-Cue.png")
screen.blit(background, (0, 0))
screen.blit(image, (100, 100))
while running:
    angle = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        angle += 90
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        if angle > 90:

        screen.blit(background, (0, 0))
        screen.blit(image, (100, 100))

    if keys[pygame.K_LEFT]:
        angle -= 90
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        x = rect.width
        screen.blit(background, (0, 0))
        screen.blit(image, (100 - x, 100))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
