__author__ = 'Stefano Bianucci'

from enemy import Enemy


class EnemyManager(object):
    """
    manager of enemy's ships
    """
    def __init__(self, surf):
        self._enemies = []
        self._surf = surf

    def add(self, x, y, e_type="a"):
        enemy = Enemy(self._surf)
        enemy.init(e_type)

        enemy.x = x
        enemy.y = y

        self._enemies.append(enemy)

        return enemy

    def update(self):
        """
        update position
        """
        flip = 0
        for en in self._enemies:
            en.update()
            if not flip:
                if en.x + en.w >= 800:
                    flip = 1
                elif en.x <= 0:
                    flip = 1
        if flip:
            for en in self._enemies:
                en.speed_x = - en.speed_x
                en.y += 80

    def render(self):
        for en in self._enemies:
            en.render()