__author__ = 'Stefano Bianucci'

from gamelib.sprite import Sprite

class Bullet(Sprite):
    """
    user shot
    """
    def __init__(self, surf):
        super(Bullet, self).__init__(surf)

        self.update_rate = 0
        self.speed_y = 0

    def init(self):
        self.load("gfx", ["fire.png"])

    def update(self):
        """
        update position
        """
        self.y += self.speed_y

    def render(self):
        self.blit()

