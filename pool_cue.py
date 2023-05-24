import pygame
import math

pygame.init()

#define screen size
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 500

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Objects")

#define colours
BG = (255, 255, 255)
BLACK = (0, 0, 0)

cue_original = pygame.image.load("Pool-Cue.png").convert_alpha()
x = 500
y = 300

#game loop
run = True
while run:

  #update background
  screen.fill(BG)

  #get mouse position
  pos = pygame.mouse.get_pos()

  #calculate turret angle
  x_dist = pos[0] - x
  y_dist = -(pos[1] - y) #-ve because pygame y coordinates increase down the screen
  angle = math.degrees(math.atan2(y_dist, x_dist))

  #rotate turret
  cue = pygame.transform.rotate(cue_original, angle - 90)
  cue_rect = cue.get_rect(center = (x, y))

  #draw image
  screen.blit(cue, cue_rect)

  #event handler
  for event in pygame.event.get():
    #quit program
    if event.type == pygame.QUIT:
      run = False

  #update display
  pygame.display.flip()

pygame.quit()
