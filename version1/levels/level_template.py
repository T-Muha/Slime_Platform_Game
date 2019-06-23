import pyglet
from pyglet.window import key
from game import platform

class LevelTemplate(dict):
    def __init__(self, dict):
        self.name = dict["Name"]
        self.batch = dict["Batch"]
        self.background = pyglet.sprite.Sprite(img=dict["Background"], x=0, y=0, batch=self.batch)
        self.platformPositions = dict["PlatformPositions"]
        self.platforms = []
        self.platformTypes = dict["PlatformTypes"]

        for position in self.platformPositions:
            self.platforms.append(platform.Platform(img=self.platformTypes[position[2]], x=position[0],y=position[1], batch=self.batch))

        for object in self.platforms:
            dict["Window"].push_handlers(object.keyHandler)

    def update(self, dt):
        for platform in self.platforms:
            platform.update(dt)

