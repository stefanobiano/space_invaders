__author__ = 'Stefano Bianucci'

import pygame
import sys

from gamelib.sprite import Sprite

# library initialization
pygame.init()

# game screen creation
screen = pygame.display.set_mode(
    (800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE)

# version of the game
pygame.display.set_caption("Version 0.3.0")

# drawing surface
surf = pygame.display.get_surface()

sprite = Sprite(surf)
sprite.load("gfx", ["player_0.png", "player_1.png"])

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


clock = pygame.time.Clock()

# cycle of game
while True:
    handle_events(pygame.event.get())

    sprite.x += dx
    sprite.y += dy

    # setting background color
    surf.fill((0, 0, 0))

    # player drawing
    sprite.blit()

    # speed setting
    clock.tick(50)

    sprite.update()

    # flip screen
    pygame.display.flip()
