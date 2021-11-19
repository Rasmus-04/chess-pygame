from varibles import *

class piece:
    def __init__(self, pos, sprite):
        self.pos = pos
        self.sprite = sprite

    def draw(self):
        win.blit(self.sprite, self.pos)
