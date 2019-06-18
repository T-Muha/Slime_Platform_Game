import pyglet
from pyglet import resource

###########################################################################
#resource file: loads and preps the sprites
###########################################################################

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

#sets anchor point to image center
def CenterImage(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

#load all of the image data
absoluteBackImage = pyglet.resource.image("absolute_back.png")
playerImage = pyglet.resource.image("player.png")
playerLeftImage = pyglet.resource.image("player_left.png")
playerLeftTwoImage = pyglet.resource.image("player_left_two.png")
playerRightImage = pyglet.resource.image("player_right.png")
playerRightTwoImage = pyglet.resource.image("player_right_two.png")
platformOneImage = pyglet.resource.image("platform_one.png")
platformTwoImage = pyglet.resource.image("platform_two.png")
playerSquashImage = pyglet.resource.image("player_squash.png")
playerLeftSquashImage = pyglet.resource.image("player_left_squash.png")
playerRightSquashImage = pyglet.resource.image("player_right_squash.png")

playerSquashImage.anchor_x += playerSquashImage.width / 10

CenterImage(platformOneImage)
CenterImage(platformTwoImage)