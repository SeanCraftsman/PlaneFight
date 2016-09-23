# -*- coding: utf8 -*-
#定义一个Bullet类，封装子弹的数据和方法

from init import *
class Bullet(object):
    def __init__(self):
        self.x = 0
        self.y = -100
        self.speed = 600
        self.image = pygame.image.load(bullet_image_filename).convert_alpha()
        self.active = False

    def move(self,passed_time_seconds):
        if self.y < 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x = mouseX - self.image.get_width()/2
            self.y = mouseY - self.image.get_width()/2
        else:
            self.y -= self.speed*passed_time_seconds

    def restart(self):
        self.active = True
        mouseX, mouseY = pygame.mouse.get_pos()
        self.x = mouseX - self.image.get_width()/2
        self.y = mouseY - self.image.get_width()/2

class Enemy(object):#定义一个Enemy类，封装敌机的数据和方法
    def restart(self):
        self.x = randint(-30,400)
        self.y = randint(-100, -50)
        self.speed = randint(100,400)
        self.active = False
    def __init__(self):
        self.restart()
        self.image = pygame.image.load(enemy_image_filename).convert_alpha()

    def move(self, passed_time_seconds):
        if self.y < 650:
            self.y += self.speed*passed_time_seconds
        else:
            self.restart()

