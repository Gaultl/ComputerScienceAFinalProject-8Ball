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
    center_x = 100
    center_y = 100
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        angle += 100
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        y = rect.height
        if abs(angle) > 90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y - y))
        else:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y))

    if keys[pygame.K_LEFT]:
        angle -= 100
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        x = rect.width
        y = rect.height
        if abs(angle) > 90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y - y))
        else:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
