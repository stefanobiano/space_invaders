__author__ = 'stefano'

import pygame
import os
import sys

# library initialization
pygame.init()

# game screen creation
screen = pygame.display.set_mode((800, 600))

# version of the game
pygame.display.set_caption("Version 0.1")

# drawing surface
surf = pygame.display.get_surface()

# player creation
player = pygame.image.load(os.path.join("gfx", "player.png"))

# player drawing
surf.blit(player, (10, 10))

# flip screen
pygame.display.flip()


def handle_events(events):
    """
    handle events

    :param events: events
    :events type: list
    """
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit(0)
        else:
            print event

# cycle of game
while True:
    handle_events(pygame.event.get())