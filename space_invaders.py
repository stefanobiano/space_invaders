__author__ = 'Stefano Bianucci'

import pygame
import sys

from spaceinv.enemy_manager import EnemyManager
from spaceinv.ship import Ship

# library initialization
pygame.init()

# game screen creation
screen = pygame.display.set_mode(
    (800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE)

# version of the game
pygame.display.set_caption("Version 0.4.0")

# drawing surface
surf = pygame.display.get_surface()

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
        elif event.type == pygame.KEYUP:
            if event.key in (275, 276):
                dx = 0
        else:
            print event

def create_enemies(em):
    row = 0
    while row < 4:
        col = 0
        while col < 4:
            em.add(col * 80, row * 80)
            col += 1
        row += 1

em = EnemyManager(surf)
create_enemies(em)

ship = Ship(surf)
ship.init()
clock = pygame.time.Clock()
ship.x = 100

# cycle of game
while True:
    handle_events(pygame.event.get())

    ship.x += dx
    # setting background color
    surf.fill((0, 0, 0))

    em.render()
    ship.render()

    # speed setting
    clock.tick(50)

    em.update()
    # flip screen
    pygame.display.flip()
