import pyglet
import json
from pyglet import resource
import time
from game import resources, platform, player
from levels import level_template

###################################################################
#main control file: starts and updates game
###################################################################


GameWindow = pyglet.window.Window(1280, 720)
bigBatch = pyglet.graphics.Batch()

testMode = False

if testMode:
    currentDict = {}
    currentDict["Name"] = "Level One"
    currentDict["Window"] = GameWindow
    currentDict["Batch"] = bigBatch
    currentDict["Background"] = resources.absoluteBackImage
    currentDict["PlatformTypes"] = [resources.testRoomFloorImage]
    currentDict["PlatformPositions"] = [[160,40,0],[480,40,0],[800,40,0],[1120,40,0]]
    currentLevel = level_template.LevelTemplate(currentDict)
else:
    currentDict = {}
    currentDict["Name"] = "Level One"
    currentDict["Window"] = GameWindow
    currentDict["Batch"] = bigBatch
    currentDict["Background"] = resources.absoluteBackImage
    currentDict["PlatformTypes"] = [resources.platformOneImage, resources.platformTwoImage]
    currentDict["PlatformPositions"] = [[225, 290, 1],[500, 320, 0],[740, 340, 0],[990, 380, 0],[1280, 220, 1],[1560, 210, 0],[1830, 220, 1],[2120, 270, 0]]
    currentLevel = level_template.LevelTemplate(currentDict)



player = player.Player(img=resources.playerImage, x=225, y=680, batch=bigBatch)
GameWindow.push_handlers(player.keyHandler)
gameObjects = [player, currentLevel]

#for object in currentLevel.platforms:
#    gameObjects.append(object)

#def update(dt):

#    for platform in platforms:
#        if platform.x - platform.width / 2 < player.x + player.width:
#            if player.x < platform.x+platform.width/2 and player.y >= platform.y+platform.height/2-20 and player.y <= platform.y+platform.height/2+10:
#                if player.falling:
#                    player.landed(platform.y+platform.height/2)
#                for object in gameObjects:
#                    object.update(dt)
#                return
#    player.fall(dt)
#    for object in gameObjects:
#        object.update(dt)

def update(dt):
    for platform in currentLevel.platforms:
        if checkLand(platform.x, platform.y, platform.width, platform.height, player.x, player.y, player.width):
            if player.falling:
                player.landed(platform.y+platform.height/2)
            for object in gameObjects:
                object.update(dt)
            return
    player.fall(dt)
    for object in gameObjects:
        object.update(dt)

def checkLand(platX, platY, platWidth, platHeight, playX, playY, playWidth):
    if platX - platWidth / 2 < playX + playWidth:
        if playX < platX + platWidth / 2 and playY >= platY + platHeight / 2 - 20 and playY <= platY + platHeight / 2 + 10:
            return True
    return False


    

@GameWindow.event
def on_draw():
    GameWindow.clear()
    bigBatch.draw()


pyglet.clock.schedule_interval(update, 1/60.0)

if __name__ == '__main__':
    pyglet.app.run()