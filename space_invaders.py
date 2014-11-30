__author__ = 'Stefano Bianucci'

import pygame
import os
import sys

# library initialization
pygame.init()

# game screen creation
screen = pygame.display.set_mode((800, 600),
                                 pygame.DOUBLEBUF | pygame.HWSURFACE)

# version of the game
pygame.display.set_caption("Version 0.2.0")

# drawing surface
surf = pygame.display.get_surface()

# player creation
player = pygame.image.load(os.path.join("gfx", "player.png"))

# movement's coordinates
dx = 0
dy = 0


def handle_events(events):
    """
    handle events

    :param events: events
    :events type: list
    """
    global dx, dy
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == 275:  # right
                dx = 1
            elif event.key == 276:  # left
                dx = -1
            elif event.key == 274:  # down
                dy = 1
            elif event.key == 273:  # up
                dy = -1
        elif event.type == pygame.KEYUP:
            if event.key in (275, 276):
                dx = 0
            elif event.key in (274, 273):
                dy = 0
        else:
            print event

x = 10
y = 10

# cycle of game
while True:
    handle_events(pygame.event.get())

    x += dx
    y += dy

    # player drawing
    surf.blit(player, (x, y))

    # flip screen
    pygame.display.flip()
