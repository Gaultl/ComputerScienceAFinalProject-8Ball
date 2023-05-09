import pygame
from tkinter import *

# window = Tk()
#
# window.title("8 - ball")
#
# window.configure(width=400, height=750)
#
# window.configure(bg='red')
# window.mainloop()

screen = pygame.display.set_mode((400, 750))
background = pygame.image.load("district.png")

screen.blit(background, (200, 375))
