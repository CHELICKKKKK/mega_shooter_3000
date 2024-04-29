import random
from pygame import *
from GameSprite import GameSprite
from random import randint

lost = 0

class Enemy(GameSprite):
    def update(self):

        self.rect.y += self.speed
        self.speed = random.randint(2, 2)
        global lost
        if self.rect.y >= 700:
           self.rect.x = random.randint(0, 500)
           self.rect.y = 0
           lost += 1


def return_lost():
    global lost
    return lost





