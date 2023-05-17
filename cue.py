import pygame

pygame.init()
screen = pygame.display.set_mode((903, 490))
pygame.display.set_caption('Loading image')

pool_cue = pygame.image.load('Pool-Cue.png')
pool_cue = pygame.transform.scale(pool_cue, (16,320))
while True:
    screen.fill("black")
    screen.blit(pool_cue, (100,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
