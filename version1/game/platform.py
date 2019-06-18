import pyglet
from pyglet.window import key
from pyglet import resource
from . import resources

class Platform(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyHandler = key.KeyStateHandler()
        self.land = [self.x-self.width/2, self.x+self.width/2, self.y+self.height/2]
        self.vx = 0



    def update(self, dt):
        left = self.keyHandler[key.LEFT] or self.keyHandler[key.A]
        right = self.keyHandler[key.RIGHT] or self.keyHandler[key.D]

        if left and right:
            self.vx = 0
        elif left:
            self.vx = 200
        elif right:
            self.vx = -200
        else:
            self.vx = 0

        self.x += self.vx * dt
        