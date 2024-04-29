import pygame.time
from pygame import *
import random
from random import randint
from Shooter1.Shooter1.Player import Player
from Shooter1.Shooter1.Enemy import Enemy, return_lost
from Shooter1.Shooter1.Bullet import Bullet

# создай окно игры
window = display.set_mode((700, 500))
display.set_caption("ГИПЕР_ШУТЕР 3000")


# задай фон сцены
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = transform.scale(image.load('rocket.png'), (100, 100))
enemy = transform.scale(image.load('rocket.png'), (700, 500))

mixer.init()
mixer.music.load('naggets-kovboj-mp3.mp3')
mixer.music.play()
fire = mixer.Sound('udar-ot-vzgliada-skaly.mp3')


font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 36)

win = font.Font(None, 36)
lose = font.Font(None, 36)

rocket = Player('rocket.png',320, 420 , 20, (60, 80), window)


monsters = sprite.Group()
ufos = []
for i in range(5):
    ufos.append(Enemy('ufo.png', random.randint(0, 700), 0,
                           random.randint(1, 4), (65, 65), window))
for i in range(5):
    monsters.add(ufos[i])


bullet = sprite.Group()

asteroid = sprite.Group()
meteor = []
for i in range(3):
    meteor.append(Enemy('asteroid.png', random.randint(0, 700), 0,
                           random.randint(1, 4), (65, 65), window))
for i in range(3):
    asteroid.add(meteor[i])

score = 0
FPS = 29
clock = time.Clock()

fire_rate = 250
last_shot = pygame.time.get_ticks()


game = True
finish = False
while game:
    # Установка ФПС
    clock.tick(FPS)
    text_lose = font1.render('Пропущено:' + str(return_lost()), 1, (255, 255, 255))
    text_kill = font2.render('Повержено:' + str(score), 1, (255, 255, 255))

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False


    if not finish:
        window.blit(background, (0, 0))

        window.blit(text_lose, (0, 0))
        window.blit(text_kill, (0, 40))

        rocket.update()

        bullet.update()
        bullet.draw(window)


        rocket.reset()
        monsters.update()
        monsters.draw(window)

        asteroid.update()
        asteroid.draw(window)



        keys_pressed = key.get_pressed()

        if keys_pressed[K_SPACE]:
            current_time = pygame.time.get_ticks()
            if current_time - last_shot >= fire_rate:
                rocket.fire(bullet, fire)
                last_shot = current_time

    sprite_list = sprite.groupcollide(bullet, monsters, True, True)
    for bulle in sprite_list:
        score += len(sprite_list[bulle])
        monsters.add(Enemy('ufo.png', random.randint(0, 700), 0,
                           random.randint(1, 4), (65, 65), window))

    if score >= 10:
        finish = True
        win_game = font1.render("YOU WIN", 6, (255, 255, 255))
        window.blit(win_game, (250, 200))
    elif return_lost() >= 3 or sprite.spritecollide(rocket, monsters, False) or sprite.spritecollide(rocket, asteroid, False):
        finish = True
        loose_game = font1.render("YOU LOSE", 7, (255, 255, 255))
        window.blit(loose_game, (250, 200))



    display.update()
