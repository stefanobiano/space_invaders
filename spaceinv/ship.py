__author__ = 'Stefano Bianucci'

from gamelib.sprite import Sprite


class Ship(Sprite):
    """
    player's ship
    """
    def __init__(self, surf):
        super(Ship, self).__init__(surf)

        self.update_rate = 0
        self.y = 560

    def init(self, bm):
        self.load("gfx", ["player_0.png"])
        self._bm = bm

    def update(self):
        """
        update position
        """
        if self.x < 5:
            self.x = 5
        if self.x > 740:
            self.x = 740

    def render(self):
        self.blit()

    def fire(self):
        """
        shot
        """
        self._bm.add(self.x + 6, self.y, -2)