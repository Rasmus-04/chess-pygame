from varibles import *

class piece:
    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite
        self.type = type

    def draw(self):
        win.blit(self.sprite, self.pos)
