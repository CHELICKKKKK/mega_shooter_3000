from GameSprite import GameSprite
from pygame import *
from Shooter1.Shooter1.Bullet import Bullet

class Player(GameSprite):
    def update(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 655 :
            self.rect.x += self.speed

    def fire(self ,group, sound):
        group.add(Bullet('bullet.png', self.rect.x+27, self.rect.y-15, 10, (15, 15), self.window))
        sound.play()