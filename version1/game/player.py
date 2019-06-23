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
        self.left = False
        self.right = False
        self.squash = False
        #previous state = unknown

    def update(self, dt):
        left = self.keyHandler[key.LEFT] or self.keyHandler[key.A]
        right = self.keyHandler[key.RIGHT] or self.keyHandler[key.D]
        up = self.keyHandler[key.UP] or self.keyHandler[key.W]
        down = self.keyHandler[key.DOWN] or self.keyHandler[key.S]

        if self.squash and not (self.left or self.right or up):
            self.image = resources.playerSquashImage
        elif not (left or right or down or self.squash):
            self.image = resources.playerImage

        if left:
            if not self.left and self.squash:
                self.image = resources.playerLeftSquashImage
            elif not self.left:
                self.image = resources.playerLeftImage
            self.left = True
            self.right = False
        elif right:
            if not self.left and self.squash:
                self.image = resources.playerRightSquashImage
            elif not self.left:
                self.image = resources.playerRightImage
            self.right = True
            self.left = False
        else:
            self.left = False
            self.right = False
            #if self.moving == True:
            #    self.moving = False
            #    self.image = resources.playerImage
        if up:
            if not self.falling and self.jumpCooled:
                self.squash = False
                self.jumpCooled = False
                pyglet.clock.schedule_once(self.coolJump, 0.1)
                self.vy += 600
            if not self.left or self.right or left or right:
                self.image = resources.playerImage
            #if self.standing:
            #    print("This condition reduces comparisions, but is it necessary?")
            #if not self.standing and left:
            #    self.image = resources.playerLeftImage
            #elif not self.standing and right:
            #    self.image = resources.playerRightImage
            #else:
            #    self.image = resources.playerImage
        if down:
            self.standing = False
            self.image = resources.playerSquashImage
            pyglet.clock.schedule_once(self.getUp, 0.5)

        self.y += self.vy * dt

    def fall(self, dt):
        self.falling = True
        if self.vy  > -600:
            self.vy = self.vy - 1200 * dt

    def landed(self, yPosition):
        self.falling = False
        self.standing = False
        self.squash = True
        self.y = yPosition
        self.vy = 0
        #if self.keyHandler[key.LEFT] or self.keyHandler[key.A]:
        #    self.image = resources.playerLeftSquashImage
        #elif self.keyHandler[key.RIGHT] or self.keyHandler[key.D]:
        #    self.image=resources.playerRightSquashImage
        #else:
        #    self.image = resources.playerSquashImage
        pyglet.clock.schedule_once(self.getUp, 0.5)
        

    def getUp(self, dt):
        self.standing = True
        self.moving = False
        self.squash = False

    def coolJump(self, dt):
        self.jumpCooled = True


