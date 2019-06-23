import pyglet
from pyglet import resource
from game import resources
from level import level_template

class LevelOne(level_template.LevelTemplate):
    def __init__(self, *args, **kwargs):
        super().__init(self, *args, **kwargs)
        
        
