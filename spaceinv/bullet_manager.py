__author__ = 'Stefano Bianucci'

from spaceinv.bullet import Bullet


class BulletManager(object):
    """
    manager of user shot
    """
    def __init__(self, surf, em):
        self._surf = surf
        self._bullets = []
        self._em = em

    def add(self, x, y, dy=-2):
        """
        create and add new shot
        """
        b = Bullet(self._surf)
        b.init()

        b.x = x
        b.y = y
        b.speed_y = dy

        self._bullets.append(b)
        return b

    def update(self):
        """
        update shot position

        if the shot goes beyond the limit
        of surf is removed

        """
        rem_list = []
        count = 0
        for b in self._bullets:
            b.update()
            if b.y >= 590:
                rem_list.append(count)

            count += 1
        rem_list.reverse()

        for b in rem_list:
            del self._bullets[b]

        self._check_collisions()

    def render(self):
        for b in self._bullets:
            b.render()

    def _check_collisions(self):
        """
        check whether the user has hit an enemy
        if yes, the shot is deleted
        """
        count = 0
        rem_list = []
        for b in self._bullets:
            obj = self._em.collide(b)
            if obj:
                rem_list.append(count)
            count += 1
        rem_list.reverse()
        for b in rem_list:
            del self._bullets[b]
