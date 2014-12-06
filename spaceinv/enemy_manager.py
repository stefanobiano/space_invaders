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
        """
        create and add new enemy
        """
        enemy = Enemy(self._surf)
        enemy.init(e_type)

        enemy.x = x
        enemy.y = y

        self._enemies.append(enemy)

        return enemy

    def update(self):
        """
        update enemy position

        if there is one enemy that moves beyond the limit
        of surf, are moved all
        this check is made for every enemy

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

    def collide(self, bullet):
        """
        check whether the user has hit an enemy
        if yes, the enemy is deleted

        :param bullet: user shot
        :return: None
        """
        count = 0
        for enemy in self._enemies:
            if enemy.is_collide(bullet):
                del self._enemies[count]
                return enemy
            count += 1
        return None