import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((903, 490))
background = pygame.image.load("Pool-Table.png")

running = True

image = pygame.image.load("Pool-Cue.png")
mov_image = pygame.image.load("Pool-Cue.png")
angle = 0
center_x = 100
center_y = 100
screen.blit(background, (0, 0))
screen.blit(image, (center_x, center_y))
x = 0
y = 0
while running:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        center_y -= 1

    if keys[pygame.K_s]:
        center_y += 1

    if keys[pygame.K_a]:
        center_x -= 1

    if keys[pygame.K_d]:
        center_x += 1

    screen.blit(background, (0, 0))
    screen.blit(image, (center_x, center_y))

    if keys[pygame.K_RIGHT]:
        angle += 1
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        y = rect.height
        x = rect.width
        if angle > 90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y - y))

        if angle < -90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y - y))

        if 0 > angle > -90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y))

        if 90 > angle > 0:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y))

    if keys[pygame.K_LEFT]:
        angle -= 1
        image = pygame.transform.rotate(mov_image, angle)
        rect = image.get_rect()
        x = rect.width
        y = rect.height
        if angle > 90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y - y))

        if angle < -90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y - y))

        if 0 > angle > -90:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x - x, center_y))

        if 90 > angle > 0:
            screen.blit(background, (0, 0))
            screen.blit(image, (center_x, center_y))

    if angle < -180:
        angle = 360 + angle

    if angle > 180:
        angle = -360 + angle

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()
pygame.quit()
