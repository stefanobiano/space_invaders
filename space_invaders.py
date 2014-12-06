__author__ = 'Stefano Bianucci'

import pygame
import sys

from spaceinv.enemy_manager import EnemyManager
from spaceinv.bullet_manager  import BulletManager
from spaceinv.ship import Ship


class Game(object):
    """
    Space invaders game
    """

    def __init__(self):

        """
        creating and running game
        """

        # library initialization
        pygame.init()

        # game screen creation
        self.screen = pygame.display.set_mode(
            (800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE)

        # version of the game
        pygame.display.set_caption("Version 0.4.0")

        # drawing surface
        self.surf = pygame.display.get_surface()

        # movement's coordinates
        self.dx = 0
        self.dy = 0

        self.components_game_creation()
        self.start_game()

    def components_game_creation(self):

        self.em = EnemyManager(self.surf)
        self.bm = BulletManager(self.surf, self.em)
        self.create_enemies(self.em)

        self.ship = Ship(self.surf)
        self.ship.init(self.bm)
        self.clock = pygame.time.Clock()
        self.ship.x = 100

    def create_enemies(self, em):
        row = 0
        while row < 4:
            col = 0
            while col < 4:
                em.add(col * 80, row * 80)
                col += 1
            row += 1

    def handle_events(self, events):
        """
        handle events

        :param events: events
        :events type: list
        """
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == 275:  # right
                    self.dx = 1
                elif event.key == 276:  # left
                    self.dx = -1
                elif event.key == 32:  # space
                    self.ship.fire()
            elif event.type == pygame.KEYUP:
                if event.key in (275, 276):
                    self.dx = 0
            else:
                print event

    def start_game(self):
        while True:
            self.handle_events(pygame.event.get())

            self.ship.x += self.dx

            # update all
            self.em.update()
            self.bm.update()
            self.ship.update()

            # setting background color
            self.surf.fill((0, 0, 0))

            # render all
            self.em.render()
            self.bm.render()
            self.ship.render()

            # speed setting
            self.clock.tick(50)

            # flip screen
            pygame.display.flip()

game = Game()