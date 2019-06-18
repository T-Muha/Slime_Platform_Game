import pyglet
from pyglet import resource
import time
from game import resources, platform, player

###################################################################
#main control file: starts and updates game
###################################################################


GameWindow = pyglet.window.Window(1280, 720)
bigBatch = pyglet.graphics.Batch()
landable = []

absoluteBack = pyglet.sprite.Sprite(img=resources.absoluteBackImage, x = 0, y = 0, batch=bigBatch)

player = player.Player(img=resources.playerImage, x=225, y=480, batch=bigBatch)
GameWindow.push_handlers(player.keyHandler)
gameObjects = [player]
platforms = []

#set up the platforms
#0 is x, 1 is y, 2 is sprite
platformPositions = [[225, 290, 2],[390, 320, 1],[520, 340, 1],[660, 380, 1],[840, 220, 2],[1010, 210, 1],[1170, 220, 2],[1350, 270, 1]]

for position in platformPositions:
    if position[2] == 1:
        platforms.append(platform.Platform(img=resources.platformOneImage, x=position[0], y=position[1], batch=bigBatch))
    elif position[2] == 2:
        platforms.append(platform.Platform(img=resources.platformTwoImage, x=position[0], y=position[1], batch=bigBatch))

gameObjects.extend(platforms)

for platform in platforms:
    GameWindow.push_handlers(platform.keyHandler)


def update(dt):
    for platform in platforms:
        if platform.x-platform.width < player.x:
            if player.x < platform.x+platform.width/2 and player.y >= platform.y+platform.height/2-5 and player.y <= platform.y+platform.height/2+10:
                if player.falling:
                    player.landed(platform.y+platform.height/2)
                for object in gameObjects:
                    object.update(dt)
                return
    player.fall(dt)
    for object in gameObjects:
        object.update(dt)
    
        

@GameWindow.event
def on_draw():
    GameWindow.clear()
    bigBatch.draw()


pyglet.clock.schedule_interval(update, 1/100.0)

if __name__ == '__main__':
    pyglet.app.run()