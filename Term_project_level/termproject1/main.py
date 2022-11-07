
# Import and initialize the pygame library
import pygame
import sys
from settings import *
from tiles import Tile
from level import Level
pygame.init()

# Set up the drawing window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)




# Run until the user asks to quit
while True:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit = ()
    screen.fill("black")
    level.run


    pygame.display.update()
    clock.tick(60)