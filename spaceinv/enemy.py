__author__ = 'Stefano Bianucci'

from gamelib.sprite import Sprite


class Enemy(Sprite):
    """
    enemy's ships
    """
    def __init__(self, surf):
        super(Enemy, self).__init__(surf)
        self.speed_x = 1

    def init(self, enemy_type="a"):
        self._type = enemy_type
        self.load("gfx", ["enemy_" + self._type + "player_0.png",
                          "enemy_" + self._type + "player_1.png"])

    def update(self):
        """
        update position
        """
        super(Enemy, self).update()
        self.x += self.speed_x

    def render(self):
        self.blit()