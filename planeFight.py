# -*- coding: utf8 -*-

background_image_filename = 'img\\background.png'
mouse_image_filename = 'img\\hero.png'
bullet_image_filename = 'img\\bullet.png'
#指定图像文件名称
 
import pygame #导入pygame库
from sys import exit #向sys模块借一个exit函数用来退出程序
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500,20) # 控制窗口打开位置

pygame.init() #初始化pygame,为使用硬件做准备
SCREEN_SIZE = (380,680)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
#创建了一个窗口
pygame.display.set_caption("PlaneFight!")
#设置窗口标题
pygame.mouse.set_visible(False) # 隐藏鼠标指针
 
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
bullet = pygame.image.load(bullet_image_filename).convert_alpha()
#加载并转换图像

bullet_x, bullet_y = 0, -100
bullet_speed = 500
clock = pygame.time.Clock()
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
    if bullet_y < -1 :
        bullet_x, bullet_y = x,y
    else:
        bullet_y -= bullet_speed * time_passed_seconds
        #print time_passed_seconds
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(bullet, (bullet_x, bullet_y))
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面