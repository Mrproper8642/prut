from pygame import *
import random
import sys
from random import *

 
font.init()
font1 = font.SysFont('Arial', 36)
 
class GameSprite(sprite.Sprite):
    def __init__(self, object_image, object_x, object_y, object_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(object_image), (size_x, size_y))
        self.speed = object_speed
        self.rect = self.image.get_rect()
        self.rect.x = object_x
        self.rect.y = object_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
    def move_rockret1(self):
        if keys_pressed[K_W] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_S] and self.rect.x < 620:
            self.rect.x += self.speed

    def move_rocket2
    if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < 620:
            self.rect.x += self.speed
 
    def update(self):
        self.rect.y += self.speed
        global lost
        global score, HpR
        if self.rect.y >= 500:
            self.rect.x = randint(20,610)
            self.rect.y = 0
            lost = lost+1
        sprites_list2 = sprite.groupcollide(
            enemyes, bullets, True, True
        )
        )
        for i in sprites_list1:
            ufo = GameSprite('ufo.png', randint(20,610), 0, randint(1,4), 100, 80)
            enemyes.add(ufo)
            if sprites_list1:
                HpR = HpR-4.5
 
 
 
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
 
class Aster(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.x = randint(20,610)
            self.rect.y = 0
            lost = lost+0.5
        global hitA
        global score
        if hitA == 0:
            sprites_list5 = sprite.groupcollide(bullets, rocks, True, True)
            for i in sprites_list5:
                self.kill()
                score += 1
 
 
 
window = display.set_mode((700, 500))
display.set_caption('Shooter')
 
bullets = sprite.Group()
 
 
 
 
clock = time.Clock()
FPS = 60
 
 
 
game = True
finish = False
 
 
 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if score >= 60:
            window.blit(gamewin, (300, 230))
            finish = True
 
        display.update()
        clock.tick(FPS)