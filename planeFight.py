# -*- coding: utf8 -*-

background_image_filename = 'img\\background.png'
mouse_image_filename = 'img\\hero.png'
bullet_image_filename = 'img\\bullet.png'
#指定图像文件名称
SCREEN_SIZE = (380,680)
 
import pygame #导入pygame库
from sys import exit #向sys模块借一个exit函数用来退出程序
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,20) # 控制窗口打开位置

#定义一个Bullet类，封装子弹的数据和方法
class Bullet(object):
    def __init__(self):
        self.x = 0
        self.y = -100
        self.speed = 600
        self.image = pygame.image.load(bullet_image_filename).convert_alpha()

    def move(self,passed_time_seconds):
        if self.y < 0:
            mouseX, mouseY = pygame.mouse.get_pos()
            self.x = mouseX - self.image.get_width()/2
            self.y = mouseY - self.image.get_width()/2
        else:
            self.y -= self.speed*passed_time_seconds


pygame.init() #初始化pygame,为使用硬件做准备
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("PlaneFight!")
pygame.mouse.set_visible(False) # 隐藏鼠标指针

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#加载并转换图像

clock = pygame.time.Clock()
bullet = Bullet()

while True:
#游戏主循环
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #接收到退出事件后退出程序
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    #将背景图画上去
    time_passed = clock.tick(100)
    time_passed_seconds = time_passed/1000.0
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    bullet.move(time_passed_seconds)

    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(bullet.image, (bullet.x, bullet.y))
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面