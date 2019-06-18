import pyglet
from pyglet.window import key
from pyglet import resource
from game import resources

class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vx = 0
        self.vy = 0
        self.keyHandler = key.KeyStateHandler()
        self.falling = False
        self.standing = True
        self.moving = False
        self.jumpCooled = True
        #previous state = unknown



    



    def update(self, dt):

        left = self.keyHandler[key.LEFT] or self.keyHandler[key.A]
        right = self.keyHandler[key.RIGHT] or self.keyHandler[key.D]
        up = self.keyHandler[key.UP] or self.keyHandler[key.W]
        down = self.keyHandler[key.DOWN] or self.keyHandler[key.S]

        if left:
            self.moving = True
            self.image = resources.playerLeftImage
        elif right:
            self.moving = True
            self.image = resources.playerRightImage
        else:
            if self.moving == True:
                self.moving = False
                self.image = resources.playerImage
        if up:
            if not self.falling and self.jumpCooled:
                self.jumpCooled = False
                pyglet.clock.schedule_once(self.coolJump, 0.1)
                self.vy += 600
            if not self.standing:
                self.image = resources.playerImage
        if down:
            self.standing = False
            self.image = resources.playerSquashImage
            pyglet.clock.schedule_once(self.getUp, 0.5)

        self.y += self.vy * dt

    def fall(self, dt):
        self.falling = True
        self.vy = self.vy - 1200 * dt

    def landed(self, yPosition):
        self.falling = False
        self.standing = False
        self.y = yPosition
        self.vy = 0
        self.image = resources.playerSquashImage
        pyglet.clock.schedule_once(self.getUp, 0.5)
        

    def getUp(self, dt):
        self.standing = True
        if not (self.keyHandler[key.DOWN] or self.keyHandler[key.S]):
            self.image = resources.playerImage

    def coolJump(self, dt):
        self.jumpCooled = True


