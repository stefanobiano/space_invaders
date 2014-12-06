__author__ = 'Stefano Bianucci'

import pygame
import os


class Sprite(object):
    """
    parent class for create game components
    """
    def __init__(self, surf):
        self._surf = surf

        # list of sprite's images
        self._images = []

        # images counter to display
        self._curr_img = 0.0

        # animation update
        self.update_rate = 0.1

        # coordinates
        self.x = 0
        self.y = 0

        # size object
        self.w = 0  # width
        self.h = 0  # height

        # Debug option
        self.debug_bounding_box = False

    def load(self, base_path, images):
        """
        Add in _images the list of images
        Save in w and in h, the width and the height of all images

        :param base_path: base path
        :base_path type: str
        :param images: images
        :images type: list
        """
        for img in images:
            self._images.append(
                pygame.image.load(os.path.join(base_path, img)))
        # all images are the same size
        self.w = self._images[0].get_width()
        self.h = self._images[0].get_height()

    def get_curr_img(self):
        """
        Get current image

        :return: image
        :return type: gif
        """
        return self._images[int(self._curr_img)]

    def update(self):
        """
        Update current image
        """
        self._curr_img += self.update_rate
        self._curr_img %= len(self._images)

    def blit(self):
        """
        Update surf
        """
        self._surf.blit(self.get_curr_img(), (self.x, self.y))
        if self.debug_bounding_box:
            pygame.draw.rect(self._surf, (255, 0, 0),
                             (self.x, self.y, self.w, self.h), 1)

    def is_collide(self, sprite):
        """
        check if the gamer has killed a enemy
        :param sprite: user shot
        :return: boolean
        """
        if (sprite.x >= self.x and sprite.x <= (self.x + self.w)) and (
            sprite.y >= self.y and sprite.y <= (self.y + self.h)):
            return True
        return False
